"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListSamplesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.samples


class ListSamplesResult(TypedDict):
    samples: NotRequired["aws_sdk_device_farm.types.samples.Samples"]
    """<p>Information about the samples.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSamplesResult) -> dict:
    out: dict = {}
    if "samples" in value:
        import aws_sdk_device_farm.types.samples

        out["samples"] = aws_sdk_device_farm.types.samples.serialize_aws_json_1_1(
            value["samples"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSamplesResult:
    out: ListSamplesResult = {}  # type: ignore[typeddict-item]
    if "samples" in data:
        import aws_sdk_device_farm.types.samples

        out["samples"] = aws_sdk_device_farm.types.samples.deserialize_aws_json_1_1(
            data["samples"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
