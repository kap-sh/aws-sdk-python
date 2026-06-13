"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetSparqlStatisticsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.statistics


class GetSparqlStatisticsOutput(TypedDict):
    status: "str"
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200. See <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html#neptune-dfe-statistics-errors\">Common error codes for DFE statistics request</a> for a list of common errors.</p> <p>When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstatisticsstatus\">neptune-db:GetStatisticsStatus</a> IAM action in that cluster.</p>"""
    payload: "aws_sdk_neptunedata.types.statistics.Statistics"
    """<p>Statistics for RDF data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSparqlStatisticsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    import aws_sdk_neptunedata.types.statistics

    out["payload"] = aws_sdk_neptunedata.types.statistics.serialize_json(
        value["payload"]
    )
    return out


def deserialize_json(data: dict) -> GetSparqlStatisticsOutput:
    out: GetSparqlStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetSparqlStatisticsOutput.status required")
    if "payload" in data:
        import aws_sdk_neptunedata.types.statistics

        out["payload"] = aws_sdk_neptunedata.types.statistics.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("GetSparqlStatisticsOutput.payload required")
    return out
