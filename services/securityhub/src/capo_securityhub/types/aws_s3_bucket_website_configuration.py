"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to
    import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules
    import capo_securityhub.types.non_empty_string


class AwsS3BucketWebsiteConfiguration(TypedDict, closed=True):
    error_document: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the error document for the website.</p>"""
    index_document_suffix: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the index document for the website.</p>"""
    redirect_all_requests_to: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to.AwsS3BucketWebsiteConfigurationRedirectTo"
    ]
    """<p>The redirect behavior for requests to the website.</p>"""
    routing_rules: NotRequired[
        "capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules.AwsS3BucketWebsiteConfigurationRoutingRules"
    ]
    """<p>The rules for applying redirects for requests to the website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfiguration) -> dict:
    out: dict = {}
    if "error_document" in value:
        out["ErrorDocument"] = value["error_document"]
    if "index_document_suffix" in value:
        out["IndexDocumentSuffix"] = value["index_document_suffix"]
    if "redirect_all_requests_to" in value:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to

        out["RedirectAllRequestsTo"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to.serialize_json(
                value["redirect_all_requests_to"]
            )
        )
    if "routing_rules" in value:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules

        out["RoutingRules"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules.serialize_json(
                value["routing_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketWebsiteConfiguration:
    out: AwsS3BucketWebsiteConfiguration = {}  # type: ignore[typeddict-item]
    if "ErrorDocument" in data:
        out["error_document"] = data["ErrorDocument"]
    if "IndexDocumentSuffix" in data:
        out["index_document_suffix"] = data["IndexDocumentSuffix"]
    if "RedirectAllRequestsTo" in data:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to

        out["redirect_all_requests_to"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_redirect_to.deserialize_json(
                data["RedirectAllRequestsTo"]
            )
        )
    if "RoutingRules" in data:
        import capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules

        out["routing_rules"] = (
            capo_securityhub.types.aws_s3_bucket_website_configuration_routing_rules.deserialize_json(
                data["RoutingRules"]
            )
        )
    return out
