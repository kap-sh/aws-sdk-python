"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTypesFromInstanceRequirementsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set
    import aws_sdk_ec2.types.string


class GetInstanceTypesFromInstanceRequirementsResult(TypedDict, closed=True):
    instance_types: NotRequired[
        "aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set.InstanceTypeInfoFromInstanceRequirementsSet"
    ]
    """<p>The instance types with the specified instance attributes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceTypesFromInstanceRequirementsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_types" in value:
        import aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set

        aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set.serialize_ec2_query(
            value["instance_types"], pairs, f"{prefix}.InstanceTypeSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> GetInstanceTypesFromInstanceRequirementsResult:
    out: GetInstanceTypesFromInstanceRequirementsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceTypeSet") is not None:
        import aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set

        out["instance_types"] = (
            aws_sdk_ec2.types.instance_type_info_from_instance_requirements_set.deserialize_ec2_query(
                el, "InstanceTypeSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
