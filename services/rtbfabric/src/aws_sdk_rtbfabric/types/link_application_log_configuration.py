"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkApplicationLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.link_application_log_sampling


class LinkApplicationLogConfiguration(TypedDict, closed=True):
    sampling: "aws_sdk_rtbfabric.types.link_application_log_sampling.LinkApplicationLogSampling"
    """<p>Describes a link application log sample.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkApplicationLogConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_rtbfabric.types.link_application_log_sampling

    out["sampling"] = (
        aws_sdk_rtbfabric.types.link_application_log_sampling.serialize_json(
            value["sampling"]
        )
    )
    return out


def deserialize_json(data: dict) -> LinkApplicationLogConfiguration:
    out: LinkApplicationLogConfiguration = {}  # type: ignore[typeddict-item]
    if "sampling" in data:
        import aws_sdk_rtbfabric.types.link_application_log_sampling

        out["sampling"] = (
            aws_sdk_rtbfabric.types.link_application_log_sampling.deserialize_json(
                data["sampling"]
            )
        )
    else:
        raise DeserializationError("LinkApplicationLogConfiguration.sampling required")
    return out
