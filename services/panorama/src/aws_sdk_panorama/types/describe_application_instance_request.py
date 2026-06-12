"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeApplicationInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id


class DescribeApplicationInstanceRequest(TypedDict):
    application_instance_id: (
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>The application instance's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeApplicationInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeApplicationInstanceRequest:
    out: DescribeApplicationInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
