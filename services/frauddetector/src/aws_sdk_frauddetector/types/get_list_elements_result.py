"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetListElementsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.elements_list
    import aws_sdk_frauddetector.types.next_token


class GetListElementsResult(TypedDict):
    elements: NotRequired["aws_sdk_frauddetector.types.elements_list.ElementsList"]
    """<p> The list elements. </p>"""
    next_token: NotRequired["aws_sdk_frauddetector.types.next_token.nextToken"]
    """<p> The next page token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetListElementsResult) -> dict:
    out: dict = {}
    if "elements" in value:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.serialize_aws_json_1_1(
                value["elements"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetListElementsResult:
    out: GetListElementsResult = {}  # type: ignore[typeddict-item]
    if "elements" in data:
        import aws_sdk_frauddetector.types.elements_list

        out["elements"] = (
            aws_sdk_frauddetector.types.elements_list.deserialize_aws_json_1_1(
                data["elements"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
