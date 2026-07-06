"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile
    import aws_sdk_customer_profiles.types.profile_id
    import aws_sdk_customer_profiles.types.query_result


class ProfileQueryResult(TypedDict, closed=True):
    profile_id: "aws_sdk_customer_profiles.types.profile_id.ProfileId"
    """<p>The profile id the result belongs to.</p>"""
    query_result: "aws_sdk_customer_profiles.types.query_result.QueryResult"
    """<p>Describes whether the profile was absent or present in the segment.</p>"""
    profile: NotRequired["aws_sdk_customer_profiles.types.profile.Profile"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQueryResult) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import aws_sdk_customer_profiles.types.query_result

    out["QueryResult"] = aws_sdk_customer_profiles.types.query_result.serialize_json(
        value["query_result"]
    )
    if "profile" in value:
        import aws_sdk_customer_profiles.types.profile

        out["Profile"] = aws_sdk_customer_profiles.types.profile.serialize_json(
            value["profile"]
        )
    return out


def deserialize_json(data: dict) -> ProfileQueryResult:
    out: ProfileQueryResult = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("ProfileQueryResult.profile_id required")
    if "QueryResult" in data:
        import aws_sdk_customer_profiles.types.query_result

        out["query_result"] = (
            aws_sdk_customer_profiles.types.query_result.deserialize_json(
                data["QueryResult"]
            )
        )
    else:
        raise DeserializationError("ProfileQueryResult.query_result required")
    if "Profile" in data:
        import aws_sdk_customer_profiles.types.profile

        out["profile"] = aws_sdk_customer_profiles.types.profile.deserialize_json(
            data["Profile"]
        )
    return out
