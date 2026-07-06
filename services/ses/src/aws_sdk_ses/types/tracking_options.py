"""Generated from Smithy shape ``com.amazonaws.ses#TrackingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.custom_redirect_domain


class TrackingOptions(TypedDict, closed=True):
    custom_redirect_domain: NotRequired[
        "aws_sdk_ses.types.custom_redirect_domain.CustomRedirectDomain"
    ]
    """<p>The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackingOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "custom_redirect_domain" in value:
        pairs.append(
            (f"{prefix}.CustomRedirectDomain", str(value["custom_redirect_domain"]))
        )


def deserialize_query(el: Element) -> TrackingOptions:
    out: TrackingOptions = {}  # type: ignore[typeddict-item]
    child_custom_redirect_domain = el.find("CustomRedirectDomain")
    if child_custom_redirect_domain is not None:
        out["custom_redirect_domain"] = str(child_custom_redirect_domain.text or "")
    return out
