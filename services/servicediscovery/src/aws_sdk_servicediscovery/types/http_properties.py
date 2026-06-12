"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HttpProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace_name


class HttpProperties(TypedDict):
    http_name: NotRequired[
        "aws_sdk_servicediscovery.types.namespace_name.NamespaceName"
    ]
    """<p>The name of an HTTP namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpProperties) -> dict:
    out: dict = {}
    if "http_name" in value:
        out["HttpName"] = value["http_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpProperties:
    out: HttpProperties = {}  # type: ignore[typeddict-item]
    if "HttpName" in data:
        out["http_name"] = data["HttpName"]
    return out
