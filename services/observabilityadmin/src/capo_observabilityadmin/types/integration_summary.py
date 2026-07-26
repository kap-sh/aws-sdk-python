"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#IntegrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.integration_status
    import capo_observabilityadmin.types.resource_arn


class IntegrationSummary(TypedDict, closed=True):
    arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the S3 Table integration.</p>"""
    status: NotRequired[
        "capo_observabilityadmin.types.integration_status.IntegrationStatus"
    ]
    """<p>The current status of the S3 Table integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status" in value:
        import capo_observabilityadmin.types.integration_status

        out["Status"] = capo_observabilityadmin.types.integration_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> IntegrationSummary:
    out: IntegrationSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Status" in data:
        import capo_observabilityadmin.types.integration_status

        out["status"] = (
            capo_observabilityadmin.types.integration_status.deserialize_json(
                data["Status"]
            )
        )
    return out
