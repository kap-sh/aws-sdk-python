"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.described_profile


class DescribeProfileResponse(TypedDict):
    profile: "aws_sdk_transfer.types.described_profile.DescribedProfile"
    """<p>The details of the specified profile, returned as an object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProfileResponse) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.described_profile

    out["Profile"] = aws_sdk_transfer.types.described_profile.serialize_aws_json_1_1(
        value["profile"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProfileResponse:
    out: DescribeProfileResponse = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        import aws_sdk_transfer.types.described_profile

        out["profile"] = (
            aws_sdk_transfer.types.described_profile.deserialize_aws_json_1_1(
                data["Profile"]
            )
        )
    else:
        raise DeserializationError("DescribeProfileResponse.profile required")
    return out
