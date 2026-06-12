"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeDataShareMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.string


class AuthorizeDataShareMessage(TypedDict):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare namespace that producers are to authorize sharing for.</p>"""
    consumer_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the data consumer that is authorized to access the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.</p>"""
    allow_writes: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If set to true, allows write operations for a datashare.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeDataShareMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "consumer_identifier" in value:
        pairs.append(
            (f"{prefix}.ConsumerIdentifier", str(value["consumer_identifier"]))
        )
    if "allow_writes" in value:
        pairs.append(
            (f"{prefix}.AllowWrites", "true" if value["allow_writes"] else "false")
        )


def deserialize_query(el: Element) -> AuthorizeDataShareMessage:
    out: AuthorizeDataShareMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_consumer_identifier = el.find("ConsumerIdentifier")
    if child_consumer_identifier is not None:
        out["consumer_identifier"] = str(child_consumer_identifier.text or "")
    child_allow_writes = el.find("AllowWrites")
    if child_allow_writes is not None:
        out["allow_writes"] = (child_allow_writes.text or "").lower() == "true"
    return out
