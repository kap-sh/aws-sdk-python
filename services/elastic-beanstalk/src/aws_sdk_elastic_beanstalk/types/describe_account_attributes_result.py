"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeAccountAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.resource_quotas


class DescribeAccountAttributesResult(TypedDict, closed=True):
    resource_quotas: NotRequired[
        "aws_sdk_elastic_beanstalk.types.resource_quotas.ResourceQuotas"
    ]
    """<p>The Elastic Beanstalk resource quotas associated with the calling AWS account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_quotas" in value:
        import aws_sdk_elastic_beanstalk.types.resource_quotas

        aws_sdk_elastic_beanstalk.types.resource_quotas.serialize_query(
            value["resource_quotas"], pairs, f"{prefix}.ResourceQuotas"
        )


def deserialize_query(el: Element) -> DescribeAccountAttributesResult:
    out: DescribeAccountAttributesResult = {}  # type: ignore[typeddict-item]
    child_resource_quotas = el.find("ResourceQuotas")
    if child_resource_quotas is not None:
        import aws_sdk_elastic_beanstalk.types.resource_quotas

        out["resource_quotas"] = (
            aws_sdk_elastic_beanstalk.types.resource_quotas.deserialize_query(
                child_resource_quotas
            )
        )
    return out
