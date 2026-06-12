from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_parse_arn,
    get_attr,
    interpolate,
    is_valid_host_label,
    parse_url,
    string_equals,
    substring,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        UseDualStack: bool | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
        AccountId: str | None = None,
        RequiresAccountId: bool | None = None,
        OutpostId: str | None = None,
        Bucket: str | None = None,
        AccessPointName: str | None = None,
        UseArnRegion: bool | None = None,
        ResourceArn: str | None = None,
        UseS3ExpressControlEndpoint: bool | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.AccountId = AccountId if AccountId is not None else None
        self.RequiresAccountId = (
            RequiresAccountId if RequiresAccountId is not None else None
        )
        self.OutpostId = OutpostId if OutpostId is not None else None
        self.Bucket = Bucket if Bucket is not None else None
        self.AccessPointName = AccessPointName if AccessPointName is not None else None
        self.UseArnRegion = UseArnRegion if UseArnRegion is not None else None
        self.ResourceArn = ResourceArn if ResourceArn is not None else None
        self.UseS3ExpressControlEndpoint = (
            UseS3ExpressControlEndpoint
            if UseS3ExpressControlEndpoint is not None
            else None
        )


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        if p.UseFIPS is True:
            _locals["partitionResult"] = aws_partition(p.Region)
            if _locals["partitionResult"] is not None:
                if string_equals(
                    get_attr(
                        _locals["partitionResult"], interpolate("name", p, _locals)
                    ),
                    interpolate("aws-cn", p, _locals),
                ):
                    raise EndpointError(
                        interpolate("Partition does not support FIPS", p, _locals)
                    )
        if p.OutpostId is not None:
            _locals["partitionResult"] = aws_partition(p.Region)
            if _locals["partitionResult"] is not None:
                if p.RequiresAccountId is not None:
                    if p.RequiresAccountId is True:
                        if not (p.AccountId is not None):
                            raise EndpointError(
                                interpolate(
                                    "AccountId is required but not set", p, _locals
                                )
                            )
                if p.AccountId is not None:
                    if not (is_valid_host_label(p.AccountId, False)):
                        raise EndpointError(
                            interpolate(
                                "AccountId must only contain a-z, A-Z, 0-9 and `-`.",
                                p,
                                _locals,
                            )
                        )
                if not (is_valid_host_label(p.OutpostId, False)):
                    raise EndpointError(
                        interpolate(
                            "OutpostId must only contain a-z, A-Z, 0-9 and `-`.",
                            p,
                            _locals,
                        )
                    )
                if p.Endpoint is not None:
                    if p.UseDualStack is True:
                        raise EndpointError(
                            interpolate(
                                "Invalid Configuration: DualStack and custom endpoint are not supported",
                                p,
                                _locals,
                            )
                        )
                if is_valid_host_label(p.Region, True):
                    if p.Endpoint is not None:
                        _locals["url"] = parse_url(p.Endpoint)
                        if _locals["url"] is not None:
                            return Endpoint(
                                url=interpolate(
                                    "{url#scheme}://{url#authority}{url#path}",
                                    p,
                                    _locals,
                                ),
                                properties={
                                    "authSchemes": [
                                        {
                                            "disableDoubleEncoding": True,
                                            "name": interpolate("sigv4", p, _locals),
                                            "signingName": interpolate(
                                                "s3-outposts", p, _locals
                                            ),
                                            "signingRegion": interpolate(
                                                "{Region}", p, _locals
                                            ),
                                        }
                                    ]
                                },
                                headers={},
                            )
                    if p.UseFIPS is True:
                        if p.UseDualStack is True:
                            return Endpoint(
                                url=interpolate(
                                    "https://s3-outposts-fips.{Region}.{partitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={
                                    "authSchemes": [
                                        {
                                            "disableDoubleEncoding": True,
                                            "name": interpolate("sigv4", p, _locals),
                                            "signingName": interpolate(
                                                "s3-outposts", p, _locals
                                            ),
                                            "signingRegion": interpolate(
                                                "{Region}", p, _locals
                                            ),
                                        }
                                    ]
                                },
                                headers={},
                            )
                    if p.UseFIPS is True:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-outposts-fips.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "s3-outposts", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                    if p.UseDualStack is True:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-outposts.{Region}.{partitionResult#dualStackDnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "s3-outposts", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                    return Endpoint(
                        url=interpolate(
                            "https://s3-outposts.{Region}.{partitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "disableDoubleEncoding": True,
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingName": interpolate(
                                        "s3-outposts", p, _locals
                                    ),
                                    "signingRegion": interpolate(
                                        "{Region}", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "Invalid region: region was not a valid DNS name.", p, _locals
                    )
                )
        if p.ResourceArn is not None:
            _locals["resourceArn"] = aws_parse_arn(p.ResourceArn)
            if _locals["resourceArn"] is not None:
                if string_equals(
                    get_attr(
                        _locals["resourceArn"], interpolate("service", p, _locals)
                    ),
                    interpolate("s3express", p, _locals),
                ):
                    _locals["partitionResult"] = aws_partition(p.Region)
                    if _locals["partitionResult"] is not None:
                        _locals["arnPartition"] = aws_partition(
                            get_attr(
                                _locals["resourceArn"],
                                interpolate("region", p, _locals),
                            )
                        )
                        if _locals["arnPartition"] is not None:
                            if string_equals(
                                get_attr(
                                    _locals["arnPartition"],
                                    interpolate("name", p, _locals),
                                ),
                                get_attr(
                                    _locals["partitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                            ):
                                if p.UseArnRegion is not None:
                                    if p.UseArnRegion is False:
                                        if not (
                                            string_equals(
                                                get_attr(
                                                    _locals["resourceArn"],
                                                    interpolate("region", p, _locals),
                                                ),
                                                interpolate("{Region}", p, _locals),
                                            )
                                        ):
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid configuration: region from ARN `{resourceArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                if p.Endpoint is not None:
                                    if p.UseDualStack is True:
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Configuration: DualStack and custom endpoint are not supported",
                                                p,
                                                _locals,
                                            )
                                        )
                                if p.UseDualStack is True:
                                    raise EndpointError(
                                        interpolate(
                                            "S3Express does not support Dual-stack.",
                                            p,
                                            _locals,
                                        )
                                    )
                                if p.Endpoint is not None:
                                    _locals["url"] = parse_url(p.Endpoint)
                                    if _locals["url"] is not None:
                                        return Endpoint(
                                            url=interpolate(
                                                "{url#scheme}://{url#authority}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                if p.UseFIPS is True:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                                return Endpoint(
                                    url=interpolate(
                                        "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "authSchemes": [
                                            {
                                                "disableDoubleEncoding": True,
                                                "name": interpolate(
                                                    "sigv4", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "s3express", p, _locals
                                                ),
                                                "signingRegion": interpolate(
                                                    "{Region}", p, _locals
                                                ),
                                            }
                                        ]
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "Client was configured for partition `{partitionResult#name}` but ARN has `{arnPartition#name}`",
                                    p,
                                    _locals,
                                )
                            )
        if p.AccessPointName is not None:
            _locals["accessPointSuffix"] = substring(p.AccessPointName, 0, 7, True)
            if _locals["accessPointSuffix"] is not None:
                if string_equals(
                    _locals["accessPointSuffix"], interpolate("--xa-s3", p, _locals)
                ):
                    _locals["partitionResult"] = aws_partition(p.Region)
                    if _locals["partitionResult"] is not None:
                        if p.Endpoint is not None:
                            if p.UseDualStack is True:
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: DualStack and custom endpoint are not supported",
                                        p,
                                        _locals,
                                    )
                                )
                        if p.UseDualStack is True:
                            raise EndpointError(
                                interpolate(
                                    "S3Express does not support Dual-stack.", p, _locals
                                )
                            )
                        if p.Endpoint is not None:
                            _locals["url"] = parse_url(p.Endpoint)
                            if _locals["url"] is not None:
                                return Endpoint(
                                    url=interpolate(
                                        "{url#scheme}://{url#authority}", p, _locals
                                    ),
                                    properties={
                                        "authSchemes": [
                                            {
                                                "disableDoubleEncoding": True,
                                                "name": interpolate(
                                                    "sigv4", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "s3express", p, _locals
                                                ),
                                                "signingRegion": interpolate(
                                                    "{Region}", p, _locals
                                                ),
                                            }
                                        ]
                                    },
                                    headers={},
                                )
                        _locals["s3expressAvailabilityZoneId"] = substring(
                            p.AccessPointName, 7, 15, True
                        )
                        if _locals["s3expressAvailabilityZoneId"] is not None:
                            _locals["s3expressAvailabilityZoneDelim"] = substring(
                                p.AccessPointName, 15, 17, True
                            )
                            if _locals["s3expressAvailabilityZoneDelim"] is not None:
                                if string_equals(
                                    _locals["s3expressAvailabilityZoneDelim"],
                                    interpolate("--", p, _locals),
                                ):
                                    if p.UseFIPS is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        _locals["s3expressAvailabilityZoneId"] = substring(
                            p.AccessPointName, 7, 16, True
                        )
                        if _locals["s3expressAvailabilityZoneId"] is not None:
                            _locals["s3expressAvailabilityZoneDelim"] = substring(
                                p.AccessPointName, 16, 18, True
                            )
                            if _locals["s3expressAvailabilityZoneDelim"] is not None:
                                if string_equals(
                                    _locals["s3expressAvailabilityZoneDelim"],
                                    interpolate("--", p, _locals),
                                ):
                                    if p.UseFIPS is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        _locals["s3expressAvailabilityZoneId"] = substring(
                            p.AccessPointName, 7, 20, True
                        )
                        if _locals["s3expressAvailabilityZoneId"] is not None:
                            _locals["s3expressAvailabilityZoneDelim"] = substring(
                                p.AccessPointName, 20, 22, True
                            )
                            if _locals["s3expressAvailabilityZoneDelim"] is not None:
                                if string_equals(
                                    _locals["s3expressAvailabilityZoneDelim"],
                                    interpolate("--", p, _locals),
                                ):
                                    if p.UseFIPS is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        _locals["s3expressAvailabilityZoneId"] = substring(
                            p.AccessPointName, 7, 21, True
                        )
                        if _locals["s3expressAvailabilityZoneId"] is not None:
                            _locals["s3expressAvailabilityZoneDelim"] = substring(
                                p.AccessPointName, 21, 23, True
                            )
                            if _locals["s3expressAvailabilityZoneDelim"] is not None:
                                if string_equals(
                                    _locals["s3expressAvailabilityZoneDelim"],
                                    interpolate("--", p, _locals),
                                ):
                                    if p.UseFIPS is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        _locals["s3expressAvailabilityZoneId"] = substring(
                            p.AccessPointName, 7, 27, True
                        )
                        if _locals["s3expressAvailabilityZoneId"] is not None:
                            _locals["s3expressAvailabilityZoneDelim"] = substring(
                                p.AccessPointName, 27, 29, True
                            )
                            if _locals["s3expressAvailabilityZoneDelim"] is not None:
                                if string_equals(
                                    _locals["s3expressAvailabilityZoneDelim"],
                                    interpolate("--", p, _locals),
                                ):
                                    if p.UseFIPS is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "authSchemes": [
                                                    {
                                                        "disableDoubleEncoding": True,
                                                        "name": interpolate(
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3express", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        raise EndpointError(
                            interpolate(
                                "Unrecognized S3Express Access Point name format.",
                                p,
                                _locals,
                            )
                        )
        if p.UseS3ExpressControlEndpoint is not None:
            if p.UseS3ExpressControlEndpoint is True:
                _locals["partitionResult"] = aws_partition(p.Region)
                if _locals["partitionResult"] is not None:
                    if p.Endpoint is not None:
                        if p.UseDualStack is True:
                            raise EndpointError(
                                interpolate(
                                    "Invalid Configuration: DualStack and custom endpoint are not supported",
                                    p,
                                    _locals,
                                )
                            )
                    if p.UseDualStack is True:
                        raise EndpointError(
                            interpolate(
                                "S3Express does not support Dual-stack.", p, _locals
                            )
                        )
                    if p.Endpoint is not None:
                        _locals["url"] = parse_url(p.Endpoint)
                        if _locals["url"] is not None:
                            return Endpoint(
                                url=interpolate(
                                    "{url#scheme}://{url#authority}", p, _locals
                                ),
                                properties={
                                    "authSchemes": [
                                        {
                                            "disableDoubleEncoding": True,
                                            "name": interpolate("sigv4", p, _locals),
                                            "signingName": interpolate(
                                                "s3express", p, _locals
                                            ),
                                            "signingRegion": interpolate(
                                                "{Region}", p, _locals
                                            ),
                                        }
                                    ]
                                },
                                headers={},
                            )
                    if p.UseFIPS is True:
                        return Endpoint(
                            url=interpolate(
                                "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "s3express", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                    return Endpoint(
                        url=interpolate(
                            "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={
                            "authSchemes": [
                                {
                                    "disableDoubleEncoding": True,
                                    "name": interpolate("sigv4", p, _locals),
                                    "signingName": interpolate("s3express", p, _locals),
                                    "signingRegion": interpolate(
                                        "{Region}", p, _locals
                                    ),
                                }
                            ]
                        },
                        headers={},
                    )
        if string_equals(p.Region, interpolate("snow", p, _locals)):
            if p.Endpoint is not None:
                _locals["url"] = parse_url(p.Endpoint)
                if _locals["url"] is not None:
                    _locals["partitionResult"] = aws_partition(p.Region)
                    if _locals["partitionResult"] is not None:
                        if p.UseDualStack is True:
                            raise EndpointError(
                                interpolate(
                                    "S3 Snow does not support DualStack", p, _locals
                                )
                            )
                        if p.UseFIPS is True:
                            raise EndpointError(
                                interpolate("S3 Snow does not support FIPS", p, _locals)
                            )
                        return Endpoint(
                            url=interpolate(
                                "{url#scheme}://{url#authority}", p, _locals
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
        if p.AccessPointName is not None:
            _locals["accessPointArn"] = aws_parse_arn(p.AccessPointName)
            if _locals["accessPointArn"] is not None:
                _locals["arnType"] = get_attr(
                    _locals["accessPointArn"], interpolate("resourceId[0]", p, _locals)
                )
                if _locals["arnType"] is not None:
                    if not (
                        string_equals(_locals["arnType"], interpolate("", p, _locals))
                    ):
                        if string_equals(
                            get_attr(
                                _locals["accessPointArn"],
                                interpolate("service", p, _locals),
                            ),
                            interpolate("s3-outposts", p, _locals),
                        ):
                            _locals["outpostId"] = get_attr(
                                _locals["accessPointArn"],
                                interpolate("resourceId[1]", p, _locals),
                            )
                            if _locals["outpostId"] is not None:
                                if is_valid_host_label(_locals["outpostId"], False):
                                    if p.Endpoint is not None:
                                        if p.UseDualStack is True:
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid Configuration: DualStack and custom endpoint are not supported",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                    if p.UseArnRegion is not None:
                                        if p.UseArnRegion is False:
                                            if not (
                                                string_equals(
                                                    get_attr(
                                                        _locals["accessPointArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    interpolate("{Region}", p, _locals),
                                                )
                                            ):
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid configuration: region from ARN `{accessPointArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                    _locals["partitionResult"] = aws_partition(p.Region)
                                    if _locals["partitionResult"] is not None:
                                        _locals["arnPartition"] = aws_partition(
                                            get_attr(
                                                _locals["accessPointArn"],
                                                interpolate("region", p, _locals),
                                            )
                                        )
                                        if _locals["arnPartition"] is not None:
                                            if string_equals(
                                                get_attr(
                                                    _locals["arnPartition"],
                                                    interpolate("name", p, _locals),
                                                ),
                                                get_attr(
                                                    _locals["partitionResult"],
                                                    interpolate("name", p, _locals),
                                                ),
                                            ):
                                                if is_valid_host_label(
                                                    get_attr(
                                                        _locals["accessPointArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    True,
                                                ):
                                                    if not (
                                                        string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "accessPointArn"
                                                                ],
                                                                interpolate(
                                                                    "accountId",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ),
                                                            interpolate("", p, _locals),
                                                        )
                                                    ):
                                                        if is_valid_host_label(
                                                            get_attr(
                                                                _locals[
                                                                    "accessPointArn"
                                                                ],
                                                                interpolate(
                                                                    "accountId",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ),
                                                            False,
                                                        ):
                                                            if p.AccountId is not None:
                                                                if not (
                                                                    string_equals(
                                                                        p.AccountId,
                                                                        interpolate(
                                                                            "{accessPointArn#accountId}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                ):
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: the accountId specified in the ARN (`{accessPointArn#accountId}`) does not match the parameter (`{AccountId}`)",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                            _locals["outpostType"] = (
                                                                get_attr(
                                                                    _locals[
                                                                        "accessPointArn"
                                                                    ],
                                                                    interpolate(
                                                                        "resourceId[2]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            )
                                                            if (
                                                                _locals["outpostType"]
                                                                is not None
                                                            ):
                                                                _locals[
                                                                    "accessPointName"
                                                                ] = get_attr(
                                                                    _locals[
                                                                        "accessPointArn"
                                                                    ],
                                                                    interpolate(
                                                                        "resourceId[3]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "accessPointName"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "outpostType"
                                                                        ],
                                                                        interpolate(
                                                                            "accesspoint",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://s3-outposts-fips.{accessPointArn#region}.{arnPartition#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={
                                                                                        "authSchemes": [
                                                                                            {
                                                                                                "disableDoubleEncoding": True,
                                                                                                "name": interpolate(
                                                                                                    "sigv4",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingName": interpolate(
                                                                                                    "s3-outposts",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingRegion": interpolate(
                                                                                                    "{accessPointArn#region}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    headers={
                                                                                        "x-amz-account-id": [
                                                                                            interpolate(
                                                                                                "{accessPointArn#accountId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                        "x-amz-outpost-id": [
                                                                                            interpolate(
                                                                                                "{outpostId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                    },
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://s3-outposts-fips.{accessPointArn#region}.{arnPartition#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={
                                                                                    "authSchemes": [
                                                                                        {
                                                                                            "disableDoubleEncoding": True,
                                                                                            "name": interpolate(
                                                                                                "sigv4",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingName": interpolate(
                                                                                                "s3-outposts",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingRegion": interpolate(
                                                                                                "{accessPointArn#region}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                headers={
                                                                                    "x-amz-account-id": [
                                                                                        interpolate(
                                                                                            "{accessPointArn#accountId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                    "x-amz-outpost-id": [
                                                                                        interpolate(
                                                                                            "{outpostId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                },
                                                                            )
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://s3-outposts.{accessPointArn#region}.{arnPartition#dualStackDnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={
                                                                                    "authSchemes": [
                                                                                        {
                                                                                            "disableDoubleEncoding": True,
                                                                                            "name": interpolate(
                                                                                                "sigv4",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingName": interpolate(
                                                                                                "s3-outposts",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingRegion": interpolate(
                                                                                                "{accessPointArn#region}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                headers={
                                                                                    "x-amz-account-id": [
                                                                                        interpolate(
                                                                                            "{accessPointArn#accountId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                    "x-amz-outpost-id": [
                                                                                        interpolate(
                                                                                            "{outpostId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                },
                                                                            )
                                                                        if (
                                                                            p.Endpoint
                                                                            is not None
                                                                        ):
                                                                            _locals[
                                                                                "url"
                                                                            ] = parse_url(
                                                                                p.Endpoint
                                                                            )
                                                                            if (
                                                                                _locals[
                                                                                    "url"
                                                                                ]
                                                                                is not None
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "{url#scheme}://{url#authority}{url#path}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={
                                                                                        "authSchemes": [
                                                                                            {
                                                                                                "disableDoubleEncoding": True,
                                                                                                "name": interpolate(
                                                                                                    "sigv4",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingName": interpolate(
                                                                                                    "s3-outposts",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingRegion": interpolate(
                                                                                                    "{accessPointArn#region}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    headers={
                                                                                        "x-amz-account-id": [
                                                                                            interpolate(
                                                                                                "{accessPointArn#accountId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                        "x-amz-outpost-id": [
                                                                                            interpolate(
                                                                                                "{outpostId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                    },
                                                                                )
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://s3-outposts.{accessPointArn#region}.{arnPartition#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={
                                                                                "authSchemes": [
                                                                                    {
                                                                                        "disableDoubleEncoding": True,
                                                                                        "name": interpolate(
                                                                                            "sigv4",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        "signingName": interpolate(
                                                                                            "s3-outposts",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        "signingRegion": interpolate(
                                                                                            "{accessPointArn#region}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    }
                                                                                ]
                                                                            },
                                                                            headers={
                                                                                "x-amz-account-id": [
                                                                                    interpolate(
                                                                                        "{accessPointArn#accountId}",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                ],
                                                                                "x-amz-outpost-id": [
                                                                                    interpolate(
                                                                                        "{outpostId}",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                ],
                                                                            },
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Expected an outpost type `accesspoint`, found `{outpostType}`",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: expected an access point name",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Invalid ARN: Expected a 4-component resource",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `{accessPointArn#accountId}`",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: missing account ID",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid region in ARN: `{accessPointArn#region}` (invalid DNS name)",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    "Client was configured for partition `{partitionResult#name}` but ARN has `{arnPartition#name}`",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: The outpost Id must only contain a-z, A-Z, 0-9 and `-`., found: `{outpostId}`",
                                        p,
                                        _locals,
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: The Outpost Id was not set",
                                    p,
                                    _locals,
                                )
                            )
                raise EndpointError(
                    interpolate("Invalid ARN: No ARN type specified", p, _locals)
                )
        if p.Bucket is not None:
            _locals["bucketArn"] = aws_parse_arn(p.Bucket)
            if _locals["bucketArn"] is not None:
                _locals["arnType"] = get_attr(
                    _locals["bucketArn"], interpolate("resourceId[0]", p, _locals)
                )
                if _locals["arnType"] is not None:
                    if not (
                        string_equals(_locals["arnType"], interpolate("", p, _locals))
                    ):
                        if string_equals(
                            get_attr(
                                _locals["bucketArn"], interpolate("service", p, _locals)
                            ),
                            interpolate("s3-outposts", p, _locals),
                        ):
                            _locals["outpostId"] = get_attr(
                                _locals["bucketArn"],
                                interpolate("resourceId[1]", p, _locals),
                            )
                            if _locals["outpostId"] is not None:
                                if is_valid_host_label(_locals["outpostId"], False):
                                    if p.Endpoint is not None:
                                        if p.UseDualStack is True:
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid Configuration: DualStack and custom endpoint are not supported",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                    if p.UseArnRegion is not None:
                                        if p.UseArnRegion is False:
                                            if not (
                                                string_equals(
                                                    get_attr(
                                                        _locals["bucketArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    interpolate("{Region}", p, _locals),
                                                )
                                            ):
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid configuration: region from ARN `{bucketArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                    _locals["arnPartition"] = aws_partition(
                                        get_attr(
                                            _locals["bucketArn"],
                                            interpolate("region", p, _locals),
                                        )
                                    )
                                    if _locals["arnPartition"] is not None:
                                        _locals["partitionResult"] = aws_partition(
                                            p.Region
                                        )
                                        if _locals["partitionResult"] is not None:
                                            if string_equals(
                                                get_attr(
                                                    _locals["arnPartition"],
                                                    interpolate("name", p, _locals),
                                                ),
                                                get_attr(
                                                    _locals["partitionResult"],
                                                    interpolate("name", p, _locals),
                                                ),
                                            ):
                                                if is_valid_host_label(
                                                    get_attr(
                                                        _locals["bucketArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    True,
                                                ):
                                                    if not (
                                                        string_equals(
                                                            get_attr(
                                                                _locals["bucketArn"],
                                                                interpolate(
                                                                    "accountId",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ),
                                                            interpolate("", p, _locals),
                                                        )
                                                    ):
                                                        if is_valid_host_label(
                                                            get_attr(
                                                                _locals["bucketArn"],
                                                                interpolate(
                                                                    "accountId",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ),
                                                            False,
                                                        ):
                                                            if p.AccountId is not None:
                                                                if not (
                                                                    string_equals(
                                                                        p.AccountId,
                                                                        interpolate(
                                                                            "{bucketArn#accountId}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                ):
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: the accountId specified in the ARN (`{bucketArn#accountId}`) does not match the parameter (`{AccountId}`)",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                            _locals["outpostType"] = (
                                                                get_attr(
                                                                    _locals[
                                                                        "bucketArn"
                                                                    ],
                                                                    interpolate(
                                                                        "resourceId[2]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            )
                                                            if (
                                                                _locals["outpostType"]
                                                                is not None
                                                            ):
                                                                _locals[
                                                                    "bucketName"
                                                                ] = get_attr(
                                                                    _locals[
                                                                        "bucketArn"
                                                                    ],
                                                                    interpolate(
                                                                        "resourceId[3]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "bucketName"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "outpostType"
                                                                        ],
                                                                        interpolate(
                                                                            "bucket",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://s3-outposts-fips.{bucketArn#region}.{arnPartition#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={
                                                                                        "authSchemes": [
                                                                                            {
                                                                                                "disableDoubleEncoding": True,
                                                                                                "name": interpolate(
                                                                                                    "sigv4",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingName": interpolate(
                                                                                                    "s3-outposts",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingRegion": interpolate(
                                                                                                    "{bucketArn#region}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    headers={
                                                                                        "x-amz-account-id": [
                                                                                            interpolate(
                                                                                                "{bucketArn#accountId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                        "x-amz-outpost-id": [
                                                                                            interpolate(
                                                                                                "{outpostId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                    },
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://s3-outposts-fips.{bucketArn#region}.{arnPartition#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={
                                                                                    "authSchemes": [
                                                                                        {
                                                                                            "disableDoubleEncoding": True,
                                                                                            "name": interpolate(
                                                                                                "sigv4",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingName": interpolate(
                                                                                                "s3-outposts",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingRegion": interpolate(
                                                                                                "{bucketArn#region}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                headers={
                                                                                    "x-amz-account-id": [
                                                                                        interpolate(
                                                                                            "{bucketArn#accountId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                    "x-amz-outpost-id": [
                                                                                        interpolate(
                                                                                            "{outpostId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                },
                                                                            )
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://s3-outposts.{bucketArn#region}.{arnPartition#dualStackDnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={
                                                                                    "authSchemes": [
                                                                                        {
                                                                                            "disableDoubleEncoding": True,
                                                                                            "name": interpolate(
                                                                                                "sigv4",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingName": interpolate(
                                                                                                "s3-outposts",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingRegion": interpolate(
                                                                                                "{bucketArn#region}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                headers={
                                                                                    "x-amz-account-id": [
                                                                                        interpolate(
                                                                                            "{bucketArn#accountId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                    "x-amz-outpost-id": [
                                                                                        interpolate(
                                                                                            "{outpostId}",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    ],
                                                                                },
                                                                            )
                                                                        if (
                                                                            p.Endpoint
                                                                            is not None
                                                                        ):
                                                                            _locals[
                                                                                "url"
                                                                            ] = parse_url(
                                                                                p.Endpoint
                                                                            )
                                                                            if (
                                                                                _locals[
                                                                                    "url"
                                                                                ]
                                                                                is not None
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "{url#scheme}://{url#authority}{url#path}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={
                                                                                        "authSchemes": [
                                                                                            {
                                                                                                "disableDoubleEncoding": True,
                                                                                                "name": interpolate(
                                                                                                    "sigv4",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingName": interpolate(
                                                                                                    "s3-outposts",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                "signingRegion": interpolate(
                                                                                                    "{bucketArn#region}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            }
                                                                                        ]
                                                                                    },
                                                                                    headers={
                                                                                        "x-amz-account-id": [
                                                                                            interpolate(
                                                                                                "{bucketArn#accountId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                        "x-amz-outpost-id": [
                                                                                            interpolate(
                                                                                                "{outpostId}",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        ],
                                                                                    },
                                                                                )
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://s3-outposts.{bucketArn#region}.{arnPartition#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={
                                                                                "authSchemes": [
                                                                                    {
                                                                                        "disableDoubleEncoding": True,
                                                                                        "name": interpolate(
                                                                                            "sigv4",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        "signingName": interpolate(
                                                                                            "s3-outposts",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        "signingRegion": interpolate(
                                                                                            "{bucketArn#region}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    }
                                                                                ]
                                                                            },
                                                                            headers={
                                                                                "x-amz-account-id": [
                                                                                    interpolate(
                                                                                        "{bucketArn#accountId}",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                ],
                                                                                "x-amz-outpost-id": [
                                                                                    interpolate(
                                                                                        "{outpostId}",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                ],
                                                                            },
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: Expected an outpost type `bucket`, found `{outpostType}`",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: expected a bucket name",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Invalid ARN: Expected a 4-component resource",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `{bucketArn#accountId}`",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: missing account ID",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid region in ARN: `{bucketArn#region}` (invalid DNS name)",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    "Client was configured for partition `{partitionResult#name}` but ARN has `{arnPartition#name}`",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: The outpost Id must only contain a-z, A-Z, 0-9 and `-`., found: `{outpostId}`",
                                        p,
                                        _locals,
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: The Outpost Id was not set",
                                    p,
                                    _locals,
                                )
                            )
                raise EndpointError(
                    interpolate("Invalid ARN: No ARN type specified", p, _locals)
                )
        _locals["partitionResult"] = aws_partition(p.Region)
        if _locals["partitionResult"] is not None:
            if is_valid_host_label(p.Region, True):
                if p.RequiresAccountId is not None:
                    if p.RequiresAccountId is True:
                        if not (p.AccountId is not None):
                            raise EndpointError(
                                interpolate(
                                    "AccountId is required but not set", p, _locals
                                )
                            )
                if p.AccountId is not None:
                    if not (is_valid_host_label(p.AccountId, False)):
                        raise EndpointError(
                            interpolate(
                                "AccountId must only contain a-z, A-Z, 0-9 and `-`.",
                                p,
                                _locals,
                            )
                        )
                if p.Endpoint is not None:
                    _locals["url"] = parse_url(p.Endpoint)
                    if _locals["url"] is not None:
                        if p.UseDualStack is True:
                            raise EndpointError(
                                interpolate(
                                    "Invalid Configuration: DualStack and custom endpoint are not supported",
                                    p,
                                    _locals,
                                )
                            )
                        if p.RequiresAccountId is not None:
                            if p.RequiresAccountId is True:
                                if p.AccountId is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "{url#scheme}://{AccountId}.{url#authority}{url#path}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                        return Endpoint(
                            url=interpolate(
                                "{url#scheme}://{url#authority}{url#path}", p, _locals
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                if p.UseFIPS is True:
                    if p.UseDualStack is True:
                        if p.RequiresAccountId is not None:
                            if p.RequiresAccountId is True:
                                if p.AccountId is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.s3-control-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                if p.UseFIPS is True:
                    if p.UseDualStack is True:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-control-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                if p.UseFIPS is True:
                    if p.UseDualStack is False:
                        if p.RequiresAccountId is not None:
                            if p.RequiresAccountId is True:
                                if p.AccountId is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.s3-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                if p.UseFIPS is True:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                if p.UseFIPS is False:
                    if p.UseDualStack is True:
                        if p.RequiresAccountId is not None:
                            if p.RequiresAccountId is True:
                                if p.AccountId is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.s3-control.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                if p.UseFIPS is False:
                    if p.UseDualStack is True:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-control.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        if p.RequiresAccountId is not None:
                            if p.RequiresAccountId is True:
                                if p.AccountId is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.s3-control.{Region}.{partitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://s3-control.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate("s3", p, _locals),
                                        "signingRegion": interpolate(
                                            "{Region}", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            raise EndpointError(
                interpolate(
                    "Invalid region: region was not a valid DNS name.", p, _locals
                )
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(interpolate("Region must be set", p, _locals))
    raise EndpointError("No endpoint rules matched")
