"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#BackendServerDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.backend_server_description

BackendServerDescriptions: TypeAlias = list[
    "capo_elastic_load_balancing.types.backend_server_description.BackendServerDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BackendServerDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.backend_server_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.backend_server_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BackendServerDescriptions:
    import capo_elastic_load_balancing.types.backend_server_description

    out: BackendServerDescriptions = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.backend_server_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: BackendServerDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.backend_server_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.backend_server_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BackendServerDescriptions:
    import capo_elastic_load_balancing.types.backend_server_description

    out: BackendServerDescriptions = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.backend_server_description.deserialize_query(
                child
            )
        )
    return out
