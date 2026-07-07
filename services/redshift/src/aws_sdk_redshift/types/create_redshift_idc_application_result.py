"""Generated from Smithy shape ``com.amazonaws.redshift#CreateRedshiftIdcApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.redshift_idc_application


class CreateRedshiftIdcApplicationResult(TypedDict, closed=True):
    redshift_idc_application: NotRequired[
        "aws_sdk_redshift.types.redshift_idc_application.RedshiftIdcApplication"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateRedshiftIdcApplicationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "redshift_idc_application" in value:
        import aws_sdk_redshift.types.redshift_idc_application

        aws_sdk_redshift.types.redshift_idc_application.serialize_query(
            value["redshift_idc_application"], pairs, f"{prefix}.RedshiftIdcApplication"
        )


def deserialize_query(el: Element) -> CreateRedshiftIdcApplicationResult:
    out: CreateRedshiftIdcApplicationResult = {}  # type: ignore[typeddict-item]
    child_redshift_idc_application = el.find("RedshiftIdcApplication")
    if child_redshift_idc_application is not None:
        import aws_sdk_redshift.types.redshift_idc_application

        out["redshift_idc_application"] = (
            aws_sdk_redshift.types.redshift_idc_application.deserialize_query(
                child_redshift_idc_application
            )
        )
    return out
