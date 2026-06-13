"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.input_source
    import aws_sdk_resiliencehubv2.types.resource


class ServiceResource(TypedDict):
    resource_identifier: "str"
    """<p>The identifier of the resource.</p>"""
    input_source: NotRequired["aws_sdk_resiliencehubv2.types.input_source.InputSource"]
    """<p>The input source that discovered the resource.</p>"""
    resource: "aws_sdk_resiliencehubv2.types.resource.Resource"
    """<p>The resource details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResource) -> dict:
    out: dict = {}
    out["resourceIdentifier"] = value["resource_identifier"]
    if "input_source" in value:
        import aws_sdk_resiliencehubv2.types.input_source

        out["inputSource"] = aws_sdk_resiliencehubv2.types.input_source.serialize_json(
            value["input_source"]
        )
    import aws_sdk_resiliencehubv2.types.resource

    out["resource"] = aws_sdk_resiliencehubv2.types.resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> ServiceResource:
    out: ServiceResource = {}  # type: ignore[typeddict-item]
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError("ServiceResource.resource_identifier required")
    if "inputSource" in data:
        import aws_sdk_resiliencehubv2.types.input_source

        out["input_source"] = (
            aws_sdk_resiliencehubv2.types.input_source.deserialize_json(
                data["inputSource"]
            )
        )
    if "resource" in data:
        import aws_sdk_resiliencehubv2.types.resource

        out["resource"] = aws_sdk_resiliencehubv2.types.resource.deserialize_json(
            data["resource"]
        )
    else:
        raise DeserializationError("ServiceResource.resource required")
    return out
