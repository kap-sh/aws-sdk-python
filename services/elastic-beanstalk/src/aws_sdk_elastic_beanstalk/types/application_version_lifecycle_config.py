"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationVersionLifecycleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.max_age_rule
    import aws_sdk_elastic_beanstalk.types.max_count_rule


class ApplicationVersionLifecycleConfig(TypedDict, closed=True):
    max_count_rule: NotRequired[
        "aws_sdk_elastic_beanstalk.types.max_count_rule.MaxCountRule"
    ]
    """<p>Specify a max count rule to restrict the number of application versions that are retained for an application.</p>"""
    max_age_rule: NotRequired["aws_sdk_elastic_beanstalk.types.max_age_rule.MaxAgeRule"]
    """<p>Specify a max age rule to restrict the length of time that application versions are retained for an application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationVersionLifecycleConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "max_count_rule" in value:
        import aws_sdk_elastic_beanstalk.types.max_count_rule

        aws_sdk_elastic_beanstalk.types.max_count_rule.serialize_query(
            value["max_count_rule"], pairs, f"{prefix}.MaxCountRule"
        )
    if "max_age_rule" in value:
        import aws_sdk_elastic_beanstalk.types.max_age_rule

        aws_sdk_elastic_beanstalk.types.max_age_rule.serialize_query(
            value["max_age_rule"], pairs, f"{prefix}.MaxAgeRule"
        )


def deserialize_query(el: Element) -> ApplicationVersionLifecycleConfig:
    out: ApplicationVersionLifecycleConfig = {}  # type: ignore[typeddict-item]
    child_max_count_rule = el.find("MaxCountRule")
    if child_max_count_rule is not None:
        import aws_sdk_elastic_beanstalk.types.max_count_rule

        out["max_count_rule"] = (
            aws_sdk_elastic_beanstalk.types.max_count_rule.deserialize_query(
                child_max_count_rule
            )
        )
    child_max_age_rule = el.find("MaxAgeRule")
    if child_max_age_rule is not None:
        import aws_sdk_elastic_beanstalk.types.max_age_rule

        out["max_age_rule"] = (
            aws_sdk_elastic_beanstalk.types.max_age_rule.deserialize_query(
                child_max_age_rule
            )
        )
    return out
