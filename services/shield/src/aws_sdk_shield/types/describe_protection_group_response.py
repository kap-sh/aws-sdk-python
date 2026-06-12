"""Generated from Smithy shape ``com.amazonaws.shield#DescribeProtectionGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group


class DescribeProtectionGroupResponse(TypedDict):
    protection_group: "aws_sdk_shield.types.protection_group.ProtectionGroup"
    """<p>A grouping of protected resources that you and Shield Advanced can monitor as a collective. This resource grouping improves the accuracy of detection and reduces false positives. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProtectionGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.protection_group

    out["ProtectionGroup"] = (
        aws_sdk_shield.types.protection_group.serialize_aws_json_1_1(
            value["protection_group"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProtectionGroupResponse:
    out: DescribeProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    if "ProtectionGroup" in data:
        import aws_sdk_shield.types.protection_group

        out["protection_group"] = (
            aws_sdk_shield.types.protection_group.deserialize_aws_json_1_1(
                data["ProtectionGroup"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProtectionGroupResponse.protection_group required"
        )
    return out
