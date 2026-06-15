"""Generated from Smithy shape ``com.amazonaws.amp#GetDefaultScraperConfigurationResponse``."""

from typing import TypedDict

from aws_sdk_amp.errors import DeserializationError


class GetDefaultScraperConfigurationResponse(TypedDict):
    configuration: "bytes"
    r"""<p>The configuration file. Base 64 encoded. For more information, see <a href=\"https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration\">Scraper configuration</a>in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultScraperConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types._prelude.blob

    out["configuration"] = aws_sdk_amp.types._prelude.blob.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> GetDefaultScraperConfigurationResponse:
    out: GetDefaultScraperConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_amp.types._prelude.blob

        out["configuration"] = aws_sdk_amp.types._prelude.blob.deserialize_json(
            data["configuration"]
        )
    else:
        raise DeserializationError(
            "GetDefaultScraperConfigurationResponse.configuration required"
        )
    return out
