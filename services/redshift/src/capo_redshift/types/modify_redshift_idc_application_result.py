"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyRedshiftIdcApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.redshift_idc_application


class ModifyRedshiftIdcApplicationResult(TypedDict, closed=True):
    redshift_idc_application: NotRequired[
        "capo_redshift.types.redshift_idc_application.RedshiftIdcApplication"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyRedshiftIdcApplicationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "redshift_idc_application" in value:
        import capo_redshift.types.redshift_idc_application

        capo_redshift.types.redshift_idc_application.serialize_query(
            value["redshift_idc_application"], pairs, f"{prefix}.RedshiftIdcApplication"
        )


def deserialize_query(el: Element) -> ModifyRedshiftIdcApplicationResult:
    out: ModifyRedshiftIdcApplicationResult = {}  # type: ignore[typeddict-item]
    child_redshift_idc_application = el.find("RedshiftIdcApplication")
    if child_redshift_idc_application is not None:
        import capo_redshift.types.redshift_idc_application

        out["redshift_idc_application"] = (
            capo_redshift.types.redshift_idc_application.deserialize_query(
                child_redshift_idc_application
            )
        )
    return out
