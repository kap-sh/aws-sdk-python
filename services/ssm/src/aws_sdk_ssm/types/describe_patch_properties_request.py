"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchPropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.operating_system
    import aws_sdk_ssm.types.patch_property
    import aws_sdk_ssm.types.patch_set


class DescribePatchPropertiesRequest(TypedDict):
    operating_system: "aws_sdk_ssm.types.operating_system.OperatingSystem"
    """<p>The operating system type for which to list patches.</p>"""
    property: "aws_sdk_ssm.types.patch_property.PatchProperty"
    """<p>The patch property for which you want to view patch details. </p>"""
    patch_set: NotRequired["aws_sdk_ssm.types.patch_set.PatchSet"]
    """<p>Indicates whether to list patches for the Windows operating system or for applications released by Microsoft. Not applicable for the Linux or macOS operating systems.</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchPropertiesRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.operating_system

    out["OperatingSystem"] = aws_sdk_ssm.types.operating_system.serialize_aws_json_1_1(
        value["operating_system"]
    )
    import aws_sdk_ssm.types.patch_property

    out["Property"] = aws_sdk_ssm.types.patch_property.serialize_aws_json_1_1(
        value["property"]
    )
    if "patch_set" in value:
        import aws_sdk_ssm.types.patch_set

        out["PatchSet"] = aws_sdk_ssm.types.patch_set.serialize_aws_json_1_1(
            value["patch_set"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchPropertiesRequest:
    out: DescribePatchPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "OperatingSystem" in data:
        import aws_sdk_ssm.types.operating_system

        out["operating_system"] = (
            aws_sdk_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePatchPropertiesRequest.operating_system required"
        )
    if "Property" in data:
        import aws_sdk_ssm.types.patch_property

        out["property"] = aws_sdk_ssm.types.patch_property.deserialize_aws_json_1_1(
            data["Property"]
        )
    else:
        raise DeserializationError("DescribePatchPropertiesRequest.property required")
    if "PatchSet" in data:
        import aws_sdk_ssm.types.patch_set

        out["patch_set"] = aws_sdk_ssm.types.patch_set.deserialize_aws_json_1_1(
            data["PatchSet"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
