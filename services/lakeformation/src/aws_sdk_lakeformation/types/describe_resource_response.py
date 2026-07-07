"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.resource_info


class DescribeResourceResponse(TypedDict, closed=True):
    resource_info: NotRequired["aws_sdk_lakeformation.types.resource_info.ResourceInfo"]
    """<p>A structure containing information about an Lake Formation resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceResponse) -> dict:
    out: dict = {}
    if "resource_info" in value:
        import aws_sdk_lakeformation.types.resource_info

        out["ResourceInfo"] = aws_sdk_lakeformation.types.resource_info.serialize_json(
            value["resource_info"]
        )
    return out


def deserialize_json(data: dict) -> DescribeResourceResponse:
    out: DescribeResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceInfo" in data:
        import aws_sdk_lakeformation.types.resource_info

        out["resource_info"] = (
            aws_sdk_lakeformation.types.resource_info.deserialize_json(
                data["ResourceInfo"]
            )
        )
    return out
