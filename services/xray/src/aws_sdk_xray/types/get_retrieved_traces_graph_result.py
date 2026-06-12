"""Generated from Smithy shape ``com.amazonaws.xray#GetRetrievedTracesGraphResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieval_status
    import aws_sdk_xray.types.retrieved_services_list
    import aws_sdk_xray.types.string


class GetRetrievedTracesGraphResult(TypedDict):
    retrieval_status: NotRequired["aws_sdk_xray.types.retrieval_status.RetrievalStatus"]
    """<p> Status of the retrieval. </p>"""
    services: NotRequired[
        "aws_sdk_xray.types.retrieved_services_list.RetrievedServicesList"
    ]
    """<p> Retrieved services. </p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrievedTracesGraphResult) -> dict:
    out: dict = {}
    if "retrieval_status" in value:
        import aws_sdk_xray.types.retrieval_status

        out["RetrievalStatus"] = aws_sdk_xray.types.retrieval_status.serialize_json(
            value["retrieval_status"]
        )
    if "services" in value:
        import aws_sdk_xray.types.retrieved_services_list

        out["Services"] = aws_sdk_xray.types.retrieved_services_list.serialize_json(
            value["services"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetRetrievedTracesGraphResult:
    out: GetRetrievedTracesGraphResult = {}  # type: ignore[typeddict-item]
    if "RetrievalStatus" in data:
        import aws_sdk_xray.types.retrieval_status

        out["retrieval_status"] = aws_sdk_xray.types.retrieval_status.deserialize_json(
            data["RetrievalStatus"]
        )
    if "Services" in data:
        import aws_sdk_xray.types.retrieved_services_list

        out["services"] = aws_sdk_xray.types.retrieved_services_list.deserialize_json(
            data["Services"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
