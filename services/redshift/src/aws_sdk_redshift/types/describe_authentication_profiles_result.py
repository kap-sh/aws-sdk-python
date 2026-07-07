"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeAuthenticationProfilesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.authentication_profile_list


class DescribeAuthenticationProfilesResult(TypedDict, closed=True):
    authentication_profiles: NotRequired[
        "aws_sdk_redshift.types.authentication_profile_list.AuthenticationProfileList"
    ]
    """<p>The list of authentication profiles.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAuthenticationProfilesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "authentication_profiles" in value:
        import aws_sdk_redshift.types.authentication_profile_list

        aws_sdk_redshift.types.authentication_profile_list.serialize_query(
            value["authentication_profiles"], pairs, f"{prefix}.AuthenticationProfiles"
        )


def deserialize_query(el: Element) -> DescribeAuthenticationProfilesResult:
    out: DescribeAuthenticationProfilesResult = {}  # type: ignore[typeddict-item]
    child_authentication_profiles = el.find("AuthenticationProfiles")
    if child_authentication_profiles is not None:
        import aws_sdk_redshift.types.authentication_profile_list

        out["authentication_profiles"] = (
            aws_sdk_redshift.types.authentication_profile_list.deserialize_query(
                child_authentication_profiles
            )
        )
    return out
