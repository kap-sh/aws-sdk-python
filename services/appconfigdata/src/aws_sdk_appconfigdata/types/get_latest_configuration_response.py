"""Generated from Smithy shape ``com.amazonaws.appconfigdata#GetLatestConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfigdata.types.integer
    import aws_sdk_appconfigdata.types.sensitive_blob
    import aws_sdk_appconfigdata.types.string
    import aws_sdk_appconfigdata.types.token


class GetLatestConfigurationResponse(TypedDict):
    next_poll_configuration_token: NotRequired[
        "aws_sdk_appconfigdata.types.token.Token"
    ]
    """<p>The latest token describing the current state of the configuration session. This <i>must</i> be provided to the next call to <code>GetLatestConfiguration.</code> </p> <important> <p>This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a <code>GetLatestConfiguration</code> call uses an expired token, the system returns <code>BadRequestException</code>.</p> </important>"""
    next_poll_interval_in_seconds: "aws_sdk_appconfigdata.types.integer.Integer"
    """<p>The amount of time the client should wait before polling for configuration updates again. Use <code>RequiredMinimumPollIntervalInSeconds</code> to set the desired poll interval.</p>"""
    content_type: NotRequired["aws_sdk_appconfigdata.types.string.String"]
    """<p>A standard MIME type describing the format of the configuration content.</p>"""
    configuration: NotRequired[
        "aws_sdk_appconfigdata.types.sensitive_blob.SensitiveBlob"
    ]
    """<p>The data of the configuration. This may be empty if the client already has the latest version of configuration.</p>"""
    version_label: NotRequired["aws_sdk_appconfigdata.types.string.String"]
    """<p>The user-defined label for the AppConfig hosted configuration version. This attribute doesn't apply if the configuration is not from an AppConfig hosted configuration version. If the client already has the latest version of the configuration data, this value is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLatestConfigurationResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_appconfigdata.types.sensitive_blob

        out["Configuration"] = (
            aws_sdk_appconfigdata.types.sensitive_blob.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLatestConfigurationResponse:
    out: GetLatestConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_appconfigdata.types.sensitive_blob

        out["configuration"] = (
            aws_sdk_appconfigdata.types.sensitive_blob.deserialize_json(
                data["Configuration"]
            )
        )
    return out
