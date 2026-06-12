"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListUploadsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.uploads


class ListUploadsResult(TypedDict):
    uploads: NotRequired["aws_sdk_device_farm.types.uploads.Uploads"]
    """<p>Information about the uploads.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUploadsResult) -> dict:
    out: dict = {}
    if "uploads" in value:
        import aws_sdk_device_farm.types.uploads

        out["uploads"] = aws_sdk_device_farm.types.uploads.serialize_aws_json_1_1(
            value["uploads"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUploadsResult:
    out: ListUploadsResult = {}  # type: ignore[typeddict-item]
    if "uploads" in data:
        import aws_sdk_device_farm.types.uploads

        out["uploads"] = aws_sdk_device_farm.types.uploads.deserialize_aws_json_1_1(
            data["uploads"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
