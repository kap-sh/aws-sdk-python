"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteRedshiftIdcApplicationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteRedshiftIdcApplicationMessage(TypedDict):
    redshift_idc_application_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The ARN for a deleted Amazon Redshift IAM Identity Center application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteRedshiftIdcApplicationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{prefix}.RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )


def deserialize_query(el: Element) -> DeleteRedshiftIdcApplicationMessage:
    out: DeleteRedshiftIdcApplicationMessage = {}  # type: ignore[typeddict-item]
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    return out
