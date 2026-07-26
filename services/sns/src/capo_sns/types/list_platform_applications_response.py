"""Generated from Smithy shape ``com.amazonaws.sns#ListPlatformApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.list_of_platform_applications
    import capo_sns.types.string


class ListPlatformApplicationsResponse(TypedDict, closed=True):
    platform_applications: NotRequired[
        "capo_sns.types.list_of_platform_applications.ListOfPlatformApplications"
    ]
    """<p>Platform applications returned when calling <code>ListPlatformApplications</code> action.</p>"""
    next_token: NotRequired["capo_sns.types.string.String"]
    """<p> <code>NextToken</code> string is returned when calling <code>ListPlatformApplications</code> action if additional records are available after the first page results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformApplicationsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_applications" in value:
        import capo_sns.types.list_of_platform_applications

        capo_sns.types.list_of_platform_applications.serialize_query(
            value["platform_applications"], pairs, f"{prefix}.PlatformApplications"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformApplicationsResponse:
    out: ListPlatformApplicationsResponse = {}  # type: ignore[typeddict-item]
    child_platform_applications = el.find("PlatformApplications")
    if child_platform_applications is not None:
        import capo_sns.types.list_of_platform_applications

        out["platform_applications"] = (
            capo_sns.types.list_of_platform_applications.deserialize_query(
                child_platform_applications
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
