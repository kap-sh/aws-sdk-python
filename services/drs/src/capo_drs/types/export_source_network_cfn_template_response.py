"""Generated from Smithy shape ``com.amazonaws.drs#ExportSourceNetworkCfnTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string


class ExportSourceNetworkCfnTemplateResponse(TypedDict, closed=True):
    s3_destination_url: NotRequired[
        "capo_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>S3 bucket URL where the Source Network CloudFormation template was exported to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportSourceNetworkCfnTemplateResponse) -> dict:
    out: dict = {}
    if "s3_destination_url" in value:
        out["s3DestinationUrl"] = value["s3_destination_url"]
    return out


def deserialize_json(data: dict) -> ExportSourceNetworkCfnTemplateResponse:
    out: ExportSourceNetworkCfnTemplateResponse = {}  # type: ignore[typeddict-item]
    if "s3DestinationUrl" in data:
        out["s3_destination_url"] = data["s3DestinationUrl"]
    return out
