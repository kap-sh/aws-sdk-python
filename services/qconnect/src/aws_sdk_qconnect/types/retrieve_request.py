"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_sensitive_string
    import aws_sdk_qconnect.types.retrieval_configuration
    import aws_sdk_qconnect.types.uuid_or_arn


class RetrieveRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant for content retrieval.</p>"""
    retrieval_configuration: (
        "aws_sdk_qconnect.types.retrieval_configuration.RetrievalConfiguration"
    )
    """<p>The configuration for the content retrieval operation.</p>"""
    retrieval_query: (
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    )
    """<p>The query for content retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveRequest) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.retrieval_configuration

    out["retrievalConfiguration"] = (
        aws_sdk_qconnect.types.retrieval_configuration.serialize_json(
            value["retrieval_configuration"]
        )
    )
    out["retrievalQuery"] = value["retrieval_query"]
    return out


def deserialize_json(data: dict) -> RetrieveRequest:
    out: RetrieveRequest = {}  # type: ignore[typeddict-item]
    if "retrievalConfiguration" in data:
        import aws_sdk_qconnect.types.retrieval_configuration

        out["retrieval_configuration"] = (
            aws_sdk_qconnect.types.retrieval_configuration.deserialize_json(
                data["retrievalConfiguration"]
            )
        )
    else:
        raise DeserializationError("RetrieveRequest.retrieval_configuration required")
    if "retrievalQuery" in data:
        out["retrieval_query"] = data["retrievalQuery"]
    else:
        raise DeserializationError("RetrieveRequest.retrieval_query required")
    return out
