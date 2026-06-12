"""Generated from Smithy shape ``com.amazonaws.mediatailor#HttpPackageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.type


class HttpPackageConfiguration(TypedDict):
    path: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The relative path to the URL for this VOD source. This is combined with <code>SourceLocation::HttpConfiguration::BaseUrl</code> to form a valid URL.</p>"""
    source_group: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source group. This has to match one of the <code>Channel::Outputs::SourceGroup</code>.</p>"""
    type: "aws_sdk_mediatailor.types.type.Type"
    """<p>The streaming protocol for this package configuration. Supported values are <code>HLS</code> and <code>DASH</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpPackageConfiguration) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    out["SourceGroup"] = value["source_group"]
    import aws_sdk_mediatailor.types.type

    out["Type"] = aws_sdk_mediatailor.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> HttpPackageConfiguration:
    out: HttpPackageConfiguration = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    else:
        raise DeserializationError("HttpPackageConfiguration.path required")
    if "SourceGroup" in data:
        out["source_group"] = data["SourceGroup"]
    else:
        raise DeserializationError("HttpPackageConfiguration.source_group required")
    if "Type" in data:
        import aws_sdk_mediatailor.types.type

        out["type"] = aws_sdk_mediatailor.types.type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("HttpPackageConfiguration.type required")
    return out
