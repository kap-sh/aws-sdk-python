"""Generated from Smithy shape ``com.amazonaws.sts#GetAccessKeyInfoResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sts.types.account_type


class GetAccessKeyInfoResponse(TypedDict):
    account: NotRequired["aws_sdk_sts.types.account_type.accountType"]
    """<p>The number used to identify the Amazon Web Services account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccessKeyInfoResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account" in value:
        pairs.append((f"{prefix}.Account", str(value["account"])))


def deserialize_query(el: Element) -> GetAccessKeyInfoResponse:
    out: GetAccessKeyInfoResponse = {}  # type: ignore[typeddict-item]
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    return out
