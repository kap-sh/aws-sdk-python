"""Generated from Smithy shape ``com.amazonaws.qconnect#ExternalSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.configuration
    import aws_sdk_qconnect.types.external_source


class ExternalSourceConfiguration(TypedDict, closed=True):
    source: "aws_sdk_qconnect.types.external_source.ExternalSource"
    """<p>The type of the external data source.</p>"""
    configuration: "aws_sdk_qconnect.types.configuration.Configuration"
    """<p>The configuration information of the external data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSourceConfiguration) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    import aws_sdk_qconnect.types.configuration

    out["configuration"] = aws_sdk_qconnect.types.configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> ExternalSourceConfiguration:
    out: ExternalSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("ExternalSourceConfiguration.source required")
    if "configuration" in data:
        import aws_sdk_qconnect.types.configuration

        out["configuration"] = aws_sdk_qconnect.types.configuration.deserialize_json(
            data["configuration"]
        )
    else:
        raise DeserializationError("ExternalSourceConfiguration.configuration required")
    return out
