"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchPropertiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_properties_list


class DescribePatchPropertiesResult(TypedDict, closed=True):
    properties: NotRequired["capo_ssm.types.patch_properties_list.PatchPropertiesList"]
    """<p>A list of the properties for patches matching the filter request parameters.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You use this token in the next call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchPropertiesResult) -> dict:
    out: dict = {}
    if "properties" in value:
        import capo_ssm.types.patch_properties_list

        out["Properties"] = capo_ssm.types.patch_properties_list.serialize_aws_json_1_1(
            value["properties"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchPropertiesResult:
    out: DescribePatchPropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("Properties") is not None:
        import capo_ssm.types.patch_properties_list

        out["properties"] = (
            capo_ssm.types.patch_properties_list.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
