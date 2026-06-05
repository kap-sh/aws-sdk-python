"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceStatement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.value_string_list


class ResourceStatement(TypedDict):
    resources: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The resources.</p>"""
    resource_types: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The resource types.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resources" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["resources"], pairs, f"{prefix}.ResourceSet"
        )
    if "resource_types" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{prefix}.ResourceTypeSet"
        )


def deserialize_ec2_query(el: Element) -> ResourceStatement:
    out: ResourceStatement = {}  # type: ignore[typeddict-item]
    if el.find("ResourceSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["resources"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "ResourceSet"
        )
    if el.find("ResourceTypeSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["resource_types"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ResourceTypeSet"
            )
        )
    return out
