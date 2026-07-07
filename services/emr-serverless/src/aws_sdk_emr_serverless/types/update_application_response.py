"""Generated from Smithy shape ``com.amazonaws.emrserverless#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application


class UpdateApplicationResponse(TypedDict, closed=True):
    application: "aws_sdk_emr_serverless.types.application.Application"
    """<p>Information about the updated application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.application

    out["application"] = aws_sdk_emr_serverless.types.application.serialize_json(
        value["application"]
    )
    return out


def deserialize_json(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "application" in data:
        import aws_sdk_emr_serverless.types.application

        out["application"] = aws_sdk_emr_serverless.types.application.deserialize_json(
            data["application"]
        )
    else:
        raise DeserializationError("UpdateApplicationResponse.application required")
    return out
