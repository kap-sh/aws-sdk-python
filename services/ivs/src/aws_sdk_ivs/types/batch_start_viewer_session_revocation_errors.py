"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_error

BatchStartViewerSessionRevocationErrors: TypeAlias = list[
    "aws_sdk_ivs.types.batch_start_viewer_session_revocation_error.BatchStartViewerSessionRevocationError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationErrors) -> list:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchStartViewerSessionRevocationErrors:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_error

    out: BatchStartViewerSessionRevocationErrors = []
    for item in data:
        out.append(
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_error.deserialize_json(
                item
            )
        )
    return out
