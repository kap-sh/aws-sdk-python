"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.endpoint
    import capo_kendra.types.endpoint_type


class ExperienceEndpoint(TypedDict, closed=True):
    endpoint_type: NotRequired["capo_kendra.types.endpoint_type.EndpointType"]
    """<p>The type of endpoint for your Amazon Kendra experience. The type currently available is <code>HOME</code>, which is a unique and fully hosted URL to the home page of your Amazon Kendra experience.</p>"""
    endpoint: NotRequired["capo_kendra.types.endpoint.Endpoint"]
    """<p>The endpoint of your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEndpoint) -> dict:
    out: dict = {}
    if "endpoint_type" in value:
        import capo_kendra.types.endpoint_type

        out["EndpointType"] = capo_kendra.types.endpoint_type.serialize_aws_json_1_1(
            value["endpoint_type"]
        )
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperienceEndpoint:
    out: ExperienceEndpoint = {}  # type: ignore[typeddict-item]
    if "EndpointType" in data:
        import capo_kendra.types.endpoint_type

        out["endpoint_type"] = capo_kendra.types.endpoint_type.deserialize_aws_json_1_1(
            data["EndpointType"]
        )
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    return out
