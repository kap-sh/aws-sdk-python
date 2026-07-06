"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ForceEndpointErrorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.endpoint_error_conditions


class ForceEndpointErrorConfiguration(TypedDict, closed=True):
    endpoint_error_conditions: NotRequired[
        "aws_sdk_mediapackagev2.types.endpoint_error_conditions.EndpointErrorConditions"
    ]
    """<p>The failover conditions for the endpoint. The options are:</p> <ul> <li> <p> <code>STALE_MANIFEST</code> - The manifest stalled and there are no new segments or parts.</p> </li> <li> <p> <code>INCOMPLETE_MANIFEST</code> - There is a gap in the manifest.</p> </li> <li> <p> <code>MISSING_DRM_KEY</code> - Key rotation is enabled but we're unable to fetch the key for the current key period.</p> </li> <li> <p> <code>SLATE_INPUT</code> - The segments which contain slate content are considered to be missing content.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForceEndpointErrorConfiguration) -> dict:
    out: dict = {}
    if "endpoint_error_conditions" in value:
        import aws_sdk_mediapackagev2.types.endpoint_error_conditions

        out["EndpointErrorConditions"] = (
            aws_sdk_mediapackagev2.types.endpoint_error_conditions.serialize_json(
                value["endpoint_error_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ForceEndpointErrorConfiguration:
    out: ForceEndpointErrorConfiguration = {}  # type: ignore[typeddict-item]
    if "EndpointErrorConditions" in data:
        import aws_sdk_mediapackagev2.types.endpoint_error_conditions

        out["endpoint_error_conditions"] = (
            aws_sdk_mediapackagev2.types.endpoint_error_conditions.deserialize_json(
                data["EndpointErrorConditions"]
            )
        )
    return out
