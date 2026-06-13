"""Generated from Smithy shape ``com.amazonaws.proton#GetResourcesSummaryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.counts_summary


class GetResourcesSummaryOutput(TypedDict):
    counts: "aws_sdk_proton.types.counts_summary.CountsSummary"
    """<p>Summary counts of each Proton resource type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcesSummaryOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.counts_summary

    out["counts"] = aws_sdk_proton.types.counts_summary.serialize_aws_json_1_0(
        value["counts"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcesSummaryOutput:
    out: GetResourcesSummaryOutput = {}  # type: ignore[typeddict-item]
    if "counts" in data:
        import aws_sdk_proton.types.counts_summary

        out["counts"] = aws_sdk_proton.types.counts_summary.deserialize_aws_json_1_0(
            data["counts"]
        )
    else:
        raise DeserializationError("GetResourcesSummaryOutput.counts required")
    return out
