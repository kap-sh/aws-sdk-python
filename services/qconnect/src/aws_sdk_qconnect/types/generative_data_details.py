"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.data_summary_list
    import aws_sdk_qconnect.types.ranking_data
    import aws_sdk_qconnect.types.sensitive_string


class GenerativeDataDetails(TypedDict, closed=True):
    completion: "aws_sdk_qconnect.types.sensitive_string.SensitiveString"
    """<p>The LLM response.</p>"""
    references: "aws_sdk_qconnect.types.data_summary_list.DataSummaryList"
    """<p>The references used to generative the LLM response.</p>"""
    ranking_data: "aws_sdk_qconnect.types.ranking_data.RankingData"
    """<p>Details about the generative content ranking data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeDataDetails) -> dict:
    out: dict = {}
    out["completion"] = value["completion"]
    import aws_sdk_qconnect.types.data_summary_list

    out["references"] = aws_sdk_qconnect.types.data_summary_list.serialize_json(
        value["references"]
    )
    import aws_sdk_qconnect.types.ranking_data

    out["rankingData"] = aws_sdk_qconnect.types.ranking_data.serialize_json(
        value["ranking_data"]
    )
    return out


def deserialize_json(data: dict) -> GenerativeDataDetails:
    out: GenerativeDataDetails = {}  # type: ignore[typeddict-item]
    if "completion" in data:
        out["completion"] = data["completion"]
    else:
        raise DeserializationError("GenerativeDataDetails.completion required")
    if "references" in data:
        import aws_sdk_qconnect.types.data_summary_list

        out["references"] = aws_sdk_qconnect.types.data_summary_list.deserialize_json(
            data["references"]
        )
    else:
        raise DeserializationError("GenerativeDataDetails.references required")
    if "rankingData" in data:
        import aws_sdk_qconnect.types.ranking_data

        out["ranking_data"] = aws_sdk_qconnect.types.ranking_data.deserialize_json(
            data["rankingData"]
        )
    else:
        raise DeserializationError("GenerativeDataDetails.ranking_data required")
    return out
