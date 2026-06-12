"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchPropertiesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.patch_properties_list


class DescribePatchPropertiesResult(TypedDict):
    properties: NotRequired[
        "aws_sdk_ssm.types.patch_properties_list.PatchPropertiesList"
    ]
    """<p>A list of the properties for patches matching the filter request parameters.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You use this token in the next call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchPropertiesResult) -> dict:
    out: dict = {}
    if "properties" in value:
        import aws_sdk_ssm.types.patch_properties_list

        out["Properties"] = (
            aws_sdk_ssm.types.patch_properties_list.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchPropertiesResult:
    out: DescribePatchPropertiesResult = {}  # type: ignore[typeddict-item]
    if "Properties" in data:
        import aws_sdk_ssm.types.patch_properties_list

        out["properties"] = (
            aws_sdk_ssm.types.patch_properties_list.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
