import unittest
from challenge_1 import Vertex, Graph


class VertexTest(unittest.TestCase):
    def test_init(self, vertex):
        label = "a"
        vertex = Vertex(label)
        assert vertex.id == "a"
        assert any(vertex.neighbors) is False

    def test_add_neighbor(self):
        label = "a"
        vertex = Vertex(label)
        vertex.add_neighbor("b", 0)
        assert any(vertex.neighbors) is True
        assert vertex.neighbors == {"b": 0}


class GraphTest(unittest.TestCase):
    def test_init(self):
        graph = Graph()
        assert any(graph.vertList) is False
        assert graph.vertCount == 0

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("a")
        assert graph.numVertices == 1
        assert "a" in graph.vertList.keys()

        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        assert graph.numVertices == 5
        graph.add_vertex("a")
        assert graph.numVertices == 5
        assert len(graph.vertList) == 5

    def test_get_vertex(self):
        graph = Graph()
        graph.add_vertex("a")
        
        assert graph.get_vertex("a")
        self.assertRaises(ValueError, graph.get_vertex, "z") 

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("a")
        graph.add_vertex("b")

        graph.add_edge("a", "b", "4")

        vertex_a = graph.get_vertex("a")
        vertex_b = graph.get_vertex("b")

        assert "b" in vertex_a.neighbors
        assert "a" in vertex_b.neighbors

        assert "b" not in vertex_b.neighbors
        assert "a" not in vertex_a.neighbors

        assert vertex_a.get_edge_weight("b") == 4
        assert vertex_b.get_edge_weight("a") == 4

        self.assertRaises(ValueError, graph.add_edge, "x", "y")

        self.assertRaises(ValueError, graph.add_edge, "a", "a")

    def test_get_vertices(self):
        graph = Graph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        assert "a" in graph.get_vertices()
        assert "b" in graph.get_vertices()
        assert "c" in graph.get_vertices()
        assert "d" in graph.get_vertices()
        assert "e" in graph.get_vertices()
        assert "x" not in graph.get_vertices()

    def test_breadth_first_search(self):
        g = Graph()

        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(4)
        g.add_vertex(5)

        g.add_edge(1, 2)
        g.add_edge(1, 4)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 5)

        g.breadth_first_search(1, 5)

        assert len(path) == 3
        assert distance == 2


if __name__ == '__main__':
    unittest.main()
