"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.value_string_list


class ResourceStatementRequest(TypedDict, closed=True):
    resources: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The resources.</p>"""
    resource_types: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The resource types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceStatementRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resources" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["resources"], pairs, f"{prefix}.Resources"
        )
    if "resource_types" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{prefix}.ResourceTypes"
        )


def deserialize_ec2_query(el: Element) -> ResourceStatementRequest:
    out: ResourceStatementRequest = {}  # type: ignore[typeddict-item]
    if el.find("Resources") is not None:
        import capo_ec2.types.value_string_list

        out["resources"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "Resources"
        )
    if el.find("ResourceTypes") is not None:
        import capo_ec2.types.value_string_list

        out["resource_types"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "ResourceTypes"
        )
    return out
