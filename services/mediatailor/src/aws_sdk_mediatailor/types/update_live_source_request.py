"""Generated from Smithy shape ``com.amazonaws.mediatailor#UpdateLiveSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.http_package_configurations


class UpdateLiveSourceRequest(TypedDict):
    http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations"
    """<p>A list of HTTP package configurations for the live source on this account.</p>"""
    live_source_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the live source.</p>"""
    source_location_name: "aws_sdk_mediatailor.types.__string.__string"
    """<p>The name of the source location associated with this Live Source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLiveSourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.http_package_configurations

    out["HttpPackageConfigurations"] = (
        aws_sdk_mediatailor.types.http_package_configurations.serialize_json(
            value["http_package_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateLiveSourceRequest:
    out: UpdateLiveSourceRequest = {}  # type: ignore[typeddict-item]
    if "HttpPackageConfigurations" in data:
        import aws_sdk_mediatailor.types.http_package_configurations

        out["http_package_configurations"] = (
            aws_sdk_mediatailor.types.http_package_configurations.deserialize_json(
                data["HttpPackageConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLiveSourceRequest.http_package_configurations required"
        )
    return out
