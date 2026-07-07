"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeApplicationInstanceDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id


class DescribeApplicationInstanceDetailsRequest(TypedDict, closed=True):
    application_instance_id: (
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>The application instance's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationInstanceDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeApplicationInstanceDetailsRequest:
    out: DescribeApplicationInstanceDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
