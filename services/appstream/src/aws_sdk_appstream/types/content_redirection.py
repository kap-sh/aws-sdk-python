"""Generated from Smithy shape ``com.amazonaws.appstream#ContentRedirection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.url_redirection_config


class ContentRedirection(TypedDict):
    host_to_client: NotRequired[
        "aws_sdk_appstream.types.url_redirection_config.UrlRedirectionConfig"
    ]
    """<p>Configuration for redirecting URLs from the remote desktop to the local client browser.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContentRedirection) -> dict:
    out: dict = {}
    if "host_to_client" in value:
        import aws_sdk_appstream.types.url_redirection_config

        out["HostToClient"] = (
            aws_sdk_appstream.types.url_redirection_config.serialize_aws_json_1_1(
                value["host_to_client"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContentRedirection:
    out: ContentRedirection = {}  # type: ignore[typeddict-item]
    if "HostToClient" in data:
        import aws_sdk_appstream.types.url_redirection_config

        out["host_to_client"] = (
            aws_sdk_appstream.types.url_redirection_config.deserialize_aws_json_1_1(
                data["HostToClient"]
            )
        )
    return out
