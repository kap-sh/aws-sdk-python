"""Generated from Smithy shape ``com.amazonaws.glue#DeleteGlueIdentityCenterConfigurationRequest``."""

from typing_extensions import TypedDict


class DeleteGlueIdentityCenterConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGlueIdentityCenterConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteGlueIdentityCenterConfigurationRequest:
    out: DeleteGlueIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
