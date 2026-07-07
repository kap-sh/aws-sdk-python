"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255


class DeleteIntegrationRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIntegrationRequest) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> DeleteIntegrationRequest:
    out: DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("DeleteIntegrationRequest.uri required")
    return out
