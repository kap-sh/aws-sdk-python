"""Generated from Smithy shape ``com.amazonaws.sts#GetSessionTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.credentials


class GetSessionTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSessionTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{prefix}.Credentials"
        )


def deserialize_query(el: Element) -> GetSessionTokenResponse:
    out: GetSessionTokenResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
    return out
