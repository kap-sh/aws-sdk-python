"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.retrieve_result_list


class RetrieveResponse(TypedDict):
    results: "aws_sdk_qconnect.types.retrieve_result_list.RetrieveResultList"
    """<p>The results of the content retrieval operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.retrieve_result_list

    out["results"] = aws_sdk_qconnect.types.retrieve_result_list.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> RetrieveResponse:
    out: RetrieveResponse = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_qconnect.types.retrieve_result_list

        out["results"] = aws_sdk_qconnect.types.retrieve_result_list.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError("RetrieveResponse.results required")
    return out
