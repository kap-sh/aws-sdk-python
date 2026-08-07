"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizedTokenIssuer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.authorized_audience_list
    import capo_redshift.types.string


class AuthorizedTokenIssuer(TypedDict, closed=True):
    trusted_token_issuer_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The ARN for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.</p>"""
    authorized_audiences_list: NotRequired[
        "capo_redshift.types.authorized_audience_list.AuthorizedAudienceList"
    ]
    """<p>The list of audiences for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizedTokenIssuer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trusted_token_issuer_arn" in value:
        pairs.append(
            (
                f"{key_prefix}TrustedTokenIssuerArn",
                str(value["trusted_token_issuer_arn"]),
            )
        )
    if "authorized_audiences_list" in value:
        import capo_redshift.types.authorized_audience_list

        capo_redshift.types.authorized_audience_list.serialize_query(
            value["authorized_audiences_list"],
            pairs,
            f"{key_prefix}AuthorizedAudiencesList",
        )


def deserialize_query(el: Element) -> AuthorizedTokenIssuer:
    out: AuthorizedTokenIssuer = {}  # type: ignore[typeddict-item]
    child_trusted_token_issuer_arn = el.find("TrustedTokenIssuerArn")
    if child_trusted_token_issuer_arn is not None:
        out["trusted_token_issuer_arn"] = str(child_trusted_token_issuer_arn.text or "")
    child_authorized_audiences_list = el.find("AuthorizedAudiencesList")
    if child_authorized_audiences_list is not None:
        import capo_redshift.types.authorized_audience_list

        out["authorized_audiences_list"] = (
            capo_redshift.types.authorized_audience_list.deserialize_query(
                child_authorized_audiences_list
            )
        )
    return out
