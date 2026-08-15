"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeApplicationStatusChecksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_response_set
    import capo_ec2.types.string


class DescribeApplicationStatusChecksResult(TypedDict, closed=True):
    application_status_checks: NotRequired[
        "capo_ec2.types.application_status_check_response_set.ApplicationStatusCheckResponseSet"
    ]
    """<p>Information about the application status checks.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeApplicationStatusChecksResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_checks" in value:
        import capo_ec2.types.application_status_check_response_set

        capo_ec2.types.application_status_check_response_set.serialize_ec2_query(
            value["application_status_checks"],
            pairs,
            f"{key_prefix}ApplicationStatusCheckSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeApplicationStatusChecksResult:
    out: DescribeApplicationStatusChecksResult = {}  # type: ignore[typeddict-item]
    child_application_status_checks = el.find("applicationStatusCheckSet")
    if child_application_status_checks is not None:
        import capo_ec2.types.application_status_check_response_set

        out["application_status_checks"] = (
            capo_ec2.types.application_status_check_response_set.deserialize_ec2_query(
                child_application_status_checks
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
