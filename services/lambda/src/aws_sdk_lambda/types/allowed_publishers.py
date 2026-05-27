"""Generated from Smithy shape ``com.amazonaws.lambda#AllowedPublishers``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.signing_profile_version_arns


class AllowedPublishers(TypedDict):
    signing_profile_version_arns: (
        "aws_sdk_lambda.types.signing_profile_version_arns.SigningProfileVersionArns"
    )
    """<p>The Amazon Resource Name (ARN) for each of the signing profiles. A signing profile defines a trusted user who can sign a code package. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedPublishers) -> dict:
    out: dict = {}
    import aws_sdk_lambda.types.signing_profile_version_arns

    out["SigningProfileVersionArns"] = (
        aws_sdk_lambda.types.signing_profile_version_arns.serialize_json(
            value["signing_profile_version_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> AllowedPublishers:
    out: AllowedPublishers = {}  # type: ignore[typeddict-item]
    if "SigningProfileVersionArns" in data:
        import aws_sdk_lambda.types.signing_profile_version_arns

        out["signing_profile_version_arns"] = (
            aws_sdk_lambda.types.signing_profile_version_arns.deserialize_json(
                data["SigningProfileVersionArns"]
            )
        )
    else:
        raise DeserializationError(
            "AllowedPublishers.signing_profile_version_arns required"
        )
    return out
