"""Generated from Smithy shape ``com.amazonaws.opensearch#CrossClusterSearchConnectionProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.skip_unavailable_status


class CrossClusterSearchConnectionProperties(TypedDict):
    skip_unavailable: NotRequired[
        "aws_sdk_opensearch.types.skip_unavailable_status.SkipUnavailableStatus"
    ]
    """<p>The status of the <code>SkipUnavailable</code> setting for the outbound connection. This feature allows you to specify some clusters as optional and ensure that your cross-cluster queries return partial results despite failures on one or more remote clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossClusterSearchConnectionProperties) -> dict:
    out: dict = {}
    if "skip_unavailable" in value:
        import aws_sdk_opensearch.types.skip_unavailable_status

        out["SkipUnavailable"] = (
            aws_sdk_opensearch.types.skip_unavailable_status.serialize_json(
                value["skip_unavailable"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrossClusterSearchConnectionProperties:
    out: CrossClusterSearchConnectionProperties = {}  # type: ignore[typeddict-item]
    if "SkipUnavailable" in data:
        import aws_sdk_opensearch.types.skip_unavailable_status

        out["skip_unavailable"] = (
            aws_sdk_opensearch.types.skip_unavailable_status.deserialize_json(
                data["SkipUnavailable"]
            )
        )
    return out
