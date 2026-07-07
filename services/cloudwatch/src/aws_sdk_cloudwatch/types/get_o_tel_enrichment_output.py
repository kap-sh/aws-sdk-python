"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetOTelEnrichmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.o_tel_enrichment_status


class GetOTelEnrichmentOutput(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_cloudwatch.types.o_tel_enrichment_status.OTelEnrichmentStatus"
    ]
    """<p>The status of OTel enrichment for the account. Valid values are <code>Running</code> (enrichment is enabled) and <code>Stopped</code> (enrichment is disabled).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOTelEnrichmentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_cloudwatch.types.o_tel_enrichment_status

        out["Status"] = (
            aws_sdk_cloudwatch.types.o_tel_enrichment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOTelEnrichmentOutput:
    out: GetOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_cloudwatch.types.o_tel_enrichment_status

        out["status"] = (
            aws_sdk_cloudwatch.types.o_tel_enrichment_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOTelEnrichmentOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_cloudwatch.types.o_tel_enrichment_status

        aws_sdk_cloudwatch.types.o_tel_enrichment_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> GetOTelEnrichmentOutput:
    out: GetOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudwatch.types.o_tel_enrichment_status

        out["status"] = (
            aws_sdk_cloudwatch.types.o_tel_enrichment_status.deserialize_query(
                child_status
            )
        )
    return out
