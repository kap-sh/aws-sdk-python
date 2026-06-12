"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisSchemeStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

AnalysisSchemeStatusList: TypeAlias = list[
    "aws_sdk_cloudsearch.types.analysis_scheme_status.AnalysisSchemeStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnalysisSchemeStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudsearch.types.analysis_scheme_status.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AnalysisSchemeStatusList:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

    out: AnalysisSchemeStatusList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudsearch.types.analysis_scheme_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AnalysisSchemeStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

    for n, item in enumerate(value, 1):
        aws_sdk_cloudsearch.types.analysis_scheme_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AnalysisSchemeStatusList:
    import aws_sdk_cloudsearch.types.analysis_scheme_status

    out: AnalysisSchemeStatusList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudsearch.types.analysis_scheme_status.deserialize_query(child)
        )
    return out
