from __future__ import annotations

from typing import Any

from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_is_virtual_hostable_s3_bucket,
    aws_parse_arn,
    get_attr,
    interpolate,
    is_valid_host_label,
    parse_url,
    string_equals,
    substring,
    uri_encode,
)

from ._aws_partition import aws_partition


class EndpointParams:
    def __init__(
        self,
        *,
        UseFIPS: bool | None = None,
        UseDualStack: bool | None = None,
        ForcePathStyle: bool | None = None,
        Accelerate: bool | None = None,
        UseGlobalEndpoint: bool | None = None,
        DisableMultiRegionAccessPoints: bool | None = None,
        Bucket: str | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
        UseObjectLambdaEndpoint: bool | None = None,
        Key: str | None = None,
        Prefix: str | None = None,
        CopySource: str | None = None,
        DisableAccessPoints: bool | None = None,
        UseArnRegion: bool | None = None,
        UseS3ExpressControlEndpoint: bool | None = None,
        DisableS3ExpressSessionAuth: bool | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.ForcePathStyle = ForcePathStyle if ForcePathStyle is not None else False
        self.Accelerate = Accelerate if Accelerate is not None else False
        self.UseGlobalEndpoint = (
            UseGlobalEndpoint if UseGlobalEndpoint is not None else False
        )
        self.DisableMultiRegionAccessPoints = (
            DisableMultiRegionAccessPoints
            if DisableMultiRegionAccessPoints is not None
            else False
        )
        self.Bucket = Bucket if Bucket is not None else None
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.UseObjectLambdaEndpoint = (
            UseObjectLambdaEndpoint if UseObjectLambdaEndpoint is not None else None
        )
        self.Key = Key if Key is not None else None
        self.Prefix = Prefix if Prefix is not None else None
        self.CopySource = CopySource if CopySource is not None else None
        self.DisableAccessPoints = (
            DisableAccessPoints if DisableAccessPoints is not None else None
        )
        self.UseArnRegion = UseArnRegion if UseArnRegion is not None else None
        self.UseS3ExpressControlEndpoint = (
            UseS3ExpressControlEndpoint
            if UseS3ExpressControlEndpoint is not None
            else None
        )
        self.DisableS3ExpressSessionAuth = (
            DisableS3ExpressSessionAuth
            if DisableS3ExpressSessionAuth is not None
            else None
        )


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        if p.Accelerate is True:
            if p.UseFIPS is True:
                raise EndpointError(
                    interpolate("Accelerate cannot be used with FIPS", p, _locals)
                )
        if p.UseDualStack is True:
            if p.Endpoint is not None:
                raise EndpointError(
                    interpolate(
                        "Cannot set dual-stack in combination with a custom endpoint.",
                        p,
                        _locals,
                    )
                )
        if p.Endpoint is not None:
            if p.UseFIPS is True:
                raise EndpointError(
                    interpolate(
                        "A custom endpoint cannot be combined with FIPS", p, _locals
                    )
                )
        if p.Endpoint is not None:
            if p.Accelerate is True:
                raise EndpointError(
                    interpolate(
                        "A custom endpoint cannot be combined with S3 Accelerate",
                        p,
                        _locals,
                    )
                )
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
        if p.Bucket is not None:
            _locals["bucketSuffix"] = substring(p.Bucket, 0, 6, True)
            if _locals["bucketSuffix"] is not None:
                if string_equals(
                    _locals["bucketSuffix"], interpolate("--x-s3", p, _locals)
                ):
                    if p.Accelerate is True:
                        raise EndpointError(
                            interpolate(
                                "S3Express does not support S3 Accelerate.", p, _locals
                            )
                        )
                    if p.Endpoint is not None:
                        _locals["url"] = parse_url(p.Endpoint)
                        if _locals["url"] is not None:
                            if p.DisableS3ExpressSessionAuth is not None:
                                if p.DisableS3ExpressSessionAuth is True:
                                    if (
                                        get_attr(
                                            _locals["url"],
                                            interpolate("isIp", p, _locals),
                                        )
                                        is True
                                    ):
                                        _locals["uri_encoded_bucket"] = uri_encode(
                                            p.Bucket
                                        )
                                        if _locals["uri_encoded_bucket"] is not None:
                                            return Endpoint(
                                                url=interpolate(
                                                    "{url#scheme}://{url#authority}/{uri_encoded_bucket}{url#path}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={
                                                    "backend": interpolate(
                                                        "S3Express", p, _locals
                                                    ),
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
                                                    ],
                                                },
                                                headers={},
                                            )
                                    if aws_is_virtual_hostable_s3_bucket(
                                        p.Bucket, False
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "{url#scheme}://{Bucket}.{url#authority}{url#path}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "backend": interpolate(
                                                    "S3Express", p, _locals
                                                ),
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
                                                ],
                                            },
                                            headers={},
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "S3Express bucket name is not a valid virtual hostable name.",
                                            p,
                                            _locals,
                                        )
                                    )
                            if (
                                get_attr(
                                    _locals["url"], interpolate("isIp", p, _locals)
                                )
                                is True
                            ):
                                _locals["uri_encoded_bucket"] = uri_encode(p.Bucket)
                                if _locals["uri_encoded_bucket"] is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "{url#scheme}://{url#authority}/{uri_encoded_bucket}{url#path}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "backend": interpolate(
                                                "S3Express", p, _locals
                                            ),
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4-s3express", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ],
                                        },
                                        headers={},
                                    )
                            if aws_is_virtual_hostable_s3_bucket(p.Bucket, False):
                                return Endpoint(
                                    url=interpolate(
                                        "{url#scheme}://{Bucket}.{url#authority}{url#path}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
                                        "authSchemes": [
                                            {
                                                "disableDoubleEncoding": True,
                                                "name": interpolate(
                                                    "sigv4-s3express", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "s3express", p, _locals
                                                ),
                                                "signingRegion": interpolate(
                                                    "{Region}", p, _locals
                                                ),
                                            }
                                        ],
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "S3Express bucket name is not a valid virtual hostable name.",
                                    p,
                                    _locals,
                                )
                            )
                    if p.UseS3ExpressControlEndpoint is not None:
                        if p.UseS3ExpressControlEndpoint is True:
                            _locals["partitionResult"] = aws_partition(p.Region)
                            if _locals["partitionResult"] is not None:
                                _locals["uri_encoded_bucket"] = uri_encode(p.Bucket)
                                if _locals["uri_encoded_bucket"] is not None:
                                    if not (p.Endpoint is not None):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://s3express-control-fips.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://s3express-control.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://s3express-control.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                    if aws_is_virtual_hostable_s3_bucket(p.Bucket, False):
                        _locals["partitionResult"] = aws_partition(p.Region)
                        if _locals["partitionResult"] is not None:
                            if p.DisableS3ExpressSessionAuth is not None:
                                if p.DisableS3ExpressSessionAuth is True:
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 6, 14, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 14, 16, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 6, 15, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 15, 17, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 6, 19, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 19, 21, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 6, 20, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 20, 22, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 6, 26, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 26, 28, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Unrecognized S3Express bucket name format.",
                                            p,
                                            _locals,
                                        )
                                    )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 6, 14, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 14, 16, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 6, 15, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 15, 17, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 6, 19, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 19, 21, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 6, 20, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 20, 22, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 6, 26, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 26, 28, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            raise EndpointError(
                                interpolate(
                                    "Unrecognized S3Express bucket name format.",
                                    p,
                                    _locals,
                                )
                            )
                    raise EndpointError(
                        interpolate(
                            "S3Express bucket name is not a valid virtual hostable name.",
                            p,
                            _locals,
                        )
                    )
        if p.Bucket is not None:
            _locals["accessPointSuffix"] = substring(p.Bucket, 0, 7, True)
            if _locals["accessPointSuffix"] is not None:
                if string_equals(
                    _locals["accessPointSuffix"], interpolate("--xa-s3", p, _locals)
                ):
                    if p.Accelerate is True:
                        raise EndpointError(
                            interpolate(
                                "S3Express does not support S3 Accelerate.", p, _locals
                            )
                        )
                    if p.Endpoint is not None:
                        _locals["url"] = parse_url(p.Endpoint)
                        if _locals["url"] is not None:
                            if p.DisableS3ExpressSessionAuth is not None:
                                if p.DisableS3ExpressSessionAuth is True:
                                    if (
                                        get_attr(
                                            _locals["url"],
                                            interpolate("isIp", p, _locals),
                                        )
                                        is True
                                    ):
                                        _locals["uri_encoded_bucket"] = uri_encode(
                                            p.Bucket
                                        )
                                        if _locals["uri_encoded_bucket"] is not None:
                                            return Endpoint(
                                                url=interpolate(
                                                    "{url#scheme}://{url#authority}/{uri_encoded_bucket}{url#path}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={
                                                    "backend": interpolate(
                                                        "S3Express", p, _locals
                                                    ),
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
                                                    ],
                                                },
                                                headers={},
                                            )
                                    if aws_is_virtual_hostable_s3_bucket(
                                        p.Bucket, False
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "{url#scheme}://{Bucket}.{url#authority}{url#path}",
                                                p,
                                                _locals,
                                            ),
                                            properties={
                                                "backend": interpolate(
                                                    "S3Express", p, _locals
                                                ),
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
                                                ],
                                            },
                                            headers={},
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "S3Express bucket name is not a valid virtual hostable name.",
                                            p,
                                            _locals,
                                        )
                                    )
                            if (
                                get_attr(
                                    _locals["url"], interpolate("isIp", p, _locals)
                                )
                                is True
                            ):
                                _locals["uri_encoded_bucket"] = uri_encode(p.Bucket)
                                if _locals["uri_encoded_bucket"] is not None:
                                    return Endpoint(
                                        url=interpolate(
                                            "{url#scheme}://{url#authority}/{uri_encoded_bucket}{url#path}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "backend": interpolate(
                                                "S3Express", p, _locals
                                            ),
                                            "authSchemes": [
                                                {
                                                    "disableDoubleEncoding": True,
                                                    "name": interpolate(
                                                        "sigv4-s3express", p, _locals
                                                    ),
                                                    "signingName": interpolate(
                                                        "s3express", p, _locals
                                                    ),
                                                    "signingRegion": interpolate(
                                                        "{Region}", p, _locals
                                                    ),
                                                }
                                            ],
                                        },
                                        headers={},
                                    )
                            if aws_is_virtual_hostable_s3_bucket(p.Bucket, False):
                                return Endpoint(
                                    url=interpolate(
                                        "{url#scheme}://{Bucket}.{url#authority}{url#path}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
                                        "authSchemes": [
                                            {
                                                "disableDoubleEncoding": True,
                                                "name": interpolate(
                                                    "sigv4-s3express", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "s3express", p, _locals
                                                ),
                                                "signingRegion": interpolate(
                                                    "{Region}", p, _locals
                                                ),
                                            }
                                        ],
                                    },
                                    headers={},
                                )
                            raise EndpointError(
                                interpolate(
                                    "S3Express bucket name is not a valid virtual hostable name.",
                                    p,
                                    _locals,
                                )
                            )
                    if aws_is_virtual_hostable_s3_bucket(p.Bucket, False):
                        _locals["partitionResult"] = aws_partition(p.Region)
                        if _locals["partitionResult"] is not None:
                            if p.DisableS3ExpressSessionAuth is not None:
                                if p.DisableS3ExpressSessionAuth is True:
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 7, 15, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 15, 17, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 7, 16, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 16, 18, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 7, 20, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 20, 22, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 7, 21, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 21, 23, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    _locals["s3expressAvailabilityZoneId"] = substring(
                                        p.Bucket, 7, 27, True
                                    )
                                    if (
                                        _locals["s3expressAvailabilityZoneId"]
                                        is not None
                                    ):
                                        _locals["s3expressAvailabilityZoneDelim"] = (
                                            substring(p.Bucket, 27, 29, True)
                                        )
                                        if (
                                            _locals["s3expressAvailabilityZoneDelim"]
                                            is not None
                                        ):
                                            if string_equals(
                                                _locals[
                                                    "s3expressAvailabilityZoneDelim"
                                                ],
                                                interpolate("--", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is True:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                                if p.UseFIPS is False:
                                                    if p.UseDualStack is False:
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "backend": interpolate(
                                                                    "S3Express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "authSchemes": [
                                                                    {
                                                                        "disableDoubleEncoding": True,
                                                                        "name": interpolate(
                                                                            "sigv4",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingName": interpolate(
                                                                            "s3express",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ],
                                                            },
                                                            headers={},
                                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Unrecognized S3Express bucket name format.",
                                            p,
                                            _locals,
                                        )
                                    )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 7, 15, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 15, 17, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 7, 16, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 16, 18, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 7, 20, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 20, 22, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 7, 21, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 21, 23, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            _locals["s3expressAvailabilityZoneId"] = substring(
                                p.Bucket, 7, 27, True
                            )
                            if _locals["s3expressAvailabilityZoneId"] is not None:
                                _locals["s3expressAvailabilityZoneDelim"] = substring(
                                    p.Bucket, 27, 29, True
                                )
                                if (
                                    _locals["s3expressAvailabilityZoneDelim"]
                                    is not None
                                ):
                                    if string_equals(
                                        _locals["s3expressAvailabilityZoneDelim"],
                                        interpolate("--", p, _locals),
                                    ):
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is True:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-fips-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is True:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                                        if p.UseFIPS is False:
                                            if p.UseDualStack is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3express-{s3expressAvailabilityZoneId}.{Region}.{partitionResult#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "backend": interpolate(
                                                            "S3Express", p, _locals
                                                        ),
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4-s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3express",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ],
                                                    },
                                                    headers={},
                                                )
                            raise EndpointError(
                                interpolate(
                                    "Unrecognized S3Express bucket name format.",
                                    p,
                                    _locals,
                                )
                            )
                    raise EndpointError(
                        interpolate(
                            "S3Express bucket name is not a valid virtual hostable name.",
                            p,
                            _locals,
                        )
                    )
        if not (p.Bucket is not None):
            if p.UseS3ExpressControlEndpoint is not None:
                if p.UseS3ExpressControlEndpoint is True:
                    _locals["partitionResult"] = aws_partition(p.Region)
                    if _locals["partitionResult"] is not None:
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
                                        "backend": interpolate("S3Express", p, _locals),
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
                                        ],
                                    },
                                    headers={},
                                )
                        if p.UseFIPS is True:
                            if p.UseDualStack is True:
                                return Endpoint(
                                    url=interpolate(
                                        "https://s3express-control-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
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
                                        ],
                                    },
                                    headers={},
                                )
                        if p.UseFIPS is True:
                            if p.UseDualStack is False:
                                return Endpoint(
                                    url=interpolate(
                                        "https://s3express-control-fips.{Region}.{partitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
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
                                        ],
                                    },
                                    headers={},
                                )
                        if p.UseFIPS is False:
                            if p.UseDualStack is True:
                                return Endpoint(
                                    url=interpolate(
                                        "https://s3express-control.dualstack.{Region}.{partitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
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
                                        ],
                                    },
                                    headers={},
                                )
                        if p.UseFIPS is False:
                            if p.UseDualStack is False:
                                return Endpoint(
                                    url=interpolate(
                                        "https://s3express-control.{Region}.{partitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={
                                        "backend": interpolate("S3Express", p, _locals),
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
                                        ],
                                    },
                                    headers={},
                                )
        if p.Bucket is not None:
            _locals["hardwareType"] = substring(p.Bucket, 49, 50, True)
            if _locals["hardwareType"] is not None:
                _locals["regionPrefix"] = substring(p.Bucket, 8, 12, True)
                if _locals["regionPrefix"] is not None:
                    _locals["bucketAliasSuffix"] = substring(p.Bucket, 0, 7, True)
                    if _locals["bucketAliasSuffix"] is not None:
                        _locals["outpostId"] = substring(p.Bucket, 32, 49, True)
                        if _locals["outpostId"] is not None:
                            _locals["regionPartition"] = aws_partition(p.Region)
                            if _locals["regionPartition"] is not None:
                                if string_equals(
                                    _locals["bucketAliasSuffix"],
                                    interpolate("--op-s3", p, _locals),
                                ):
                                    if is_valid_host_label(_locals["outpostId"], False):
                                        if aws_is_virtual_hostable_s3_bucket(
                                            p.Bucket, False
                                        ):
                                            if string_equals(
                                                _locals["hardwareType"],
                                                interpolate("e", p, _locals),
                                            ):
                                                if string_equals(
                                                    _locals["regionPrefix"],
                                                    interpolate("beta", p, _locals),
                                                ):
                                                    if not (p.Endpoint is not None):
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Expected a endpoint to be specified but no endpoint was found",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    if p.Endpoint is not None:
                                                        _locals["url"] = parse_url(
                                                            p.Endpoint
                                                        )
                                                        if _locals["url"] is not None:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{Bucket}.ec2.{url#authority}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={
                                                                    "authSchemes": [
                                                                        {
                                                                            "disableDoubleEncoding": True,
                                                                            "name": interpolate(
                                                                                "sigv4a",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingName": interpolate(
                                                                                "s3-outposts",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegionSet": [
                                                                                interpolate(
                                                                                    "*",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            ],
                                                                        },
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
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        },
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.ec2.s3-outposts.{Region}.{regionPartition#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4a", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3-outposts",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegionSet": [
                                                                    interpolate(
                                                                        "*", p, _locals
                                                                    )
                                                                ],
                                                            },
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3-outposts",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            },
                                                        ]
                                                    },
                                                    headers={},
                                                )
                                            if string_equals(
                                                _locals["hardwareType"],
                                                interpolate("o", p, _locals),
                                            ):
                                                if string_equals(
                                                    _locals["regionPrefix"],
                                                    interpolate("beta", p, _locals),
                                                ):
                                                    if not (p.Endpoint is not None):
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Expected a endpoint to be specified but no endpoint was found",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    if p.Endpoint is not None:
                                                        _locals["url"] = parse_url(
                                                            p.Endpoint
                                                        )
                                                        if _locals["url"] is not None:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{Bucket}.op-{outpostId}.{url#authority}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={
                                                                    "authSchemes": [
                                                                        {
                                                                            "disableDoubleEncoding": True,
                                                                            "name": interpolate(
                                                                                "sigv4a",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingName": interpolate(
                                                                                "s3-outposts",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegionSet": [
                                                                                interpolate(
                                                                                    "*",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            ],
                                                                        },
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
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        },
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.op-{outpostId}.s3-outposts.{Region}.{regionPartition#dnsSuffix}",
                                                        p,
                                                        _locals,
                                                    ),
                                                    properties={
                                                        "authSchemes": [
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4a", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3-outposts",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegionSet": [
                                                                    interpolate(
                                                                        "*", p, _locals
                                                                    )
                                                                ],
                                                            },
                                                            {
                                                                "disableDoubleEncoding": True,
                                                                "name": interpolate(
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3-outposts",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            },
                                                        ]
                                                    },
                                                    headers={},
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    'Unrecognized hardware type: "Expected hardware type o or e but got {hardwareType}"',
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Outposts Bucket alias - it must be a valid bucket name.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: The outpost Id must only contain a-z, A-Z, 0-9 and `-`.",
                                            p,
                                            _locals,
                                        )
                                    )
        if p.Bucket is not None:
            if p.Endpoint is not None:
                if not (parse_url(p.Endpoint) is not None):
                    raise EndpointError(
                        interpolate(
                            "Custom endpoint `{Endpoint}` was not a valid URI",
                            p,
                            _locals,
                        )
                    )
            if p.ForcePathStyle is False:
                if aws_is_virtual_hostable_s3_bucket(p.Bucket, False):
                    _locals["partitionResult"] = aws_partition(p.Region)
                    if _locals["partitionResult"] is not None:
                        if is_valid_host_label(p.Region, False):
                            if p.Accelerate is True:
                                if string_equals(
                                    get_attr(
                                        _locals["partitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-cn", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "S3 Accelerate cannot be used in this region",
                                            p,
                                            _locals,
                                        )
                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3-fips.dualstack.us-east-1.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is True:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3-fips.us-east-1.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is False:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-fips.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is True:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-fips.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3-accelerate.dualstack.us-east-1.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-accelerate.dualstack.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-accelerate.dualstack.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3.dualstack.us-east-1.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is True:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is True
                                                ):
                                                    if string_equals(
                                                        p.Region,
                                                        interpolate(
                                                            "aws-global", p, _locals
                                                        ),
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "{url#scheme}://{url#authority}{url#normalizedPath}{Bucket}",
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
                                                                            "s3",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "us-east-1",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ]
                                                            },
                                                            headers={},
                                                        )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is False
                                                ):
                                                    if string_equals(
                                                        p.Region,
                                                        interpolate(
                                                            "aws-global", p, _locals
                                                        ),
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "{url#scheme}://{Bucket}.{url#authority}{url#path}",
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
                                                                            "s3",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "us-east-1",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ]
                                                            },
                                                            headers={},
                                                        )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is True
                                                ):
                                                    if not (
                                                        string_equals(
                                                            p.Region,
                                                            interpolate(
                                                                "aws-global", p, _locals
                                                            ),
                                                        )
                                                    ):
                                                        if p.UseGlobalEndpoint is True:
                                                            if string_equals(
                                                                p.Region,
                                                                interpolate(
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ):
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "{url#scheme}://{url#authority}{url#normalizedPath}{Bucket}",
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
                                                                                    "s3",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                "signingRegion": interpolate(
                                                                                    "{Region}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            }
                                                                        ]
                                                                    },
                                                                    headers={},
                                                                )
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "{url#scheme}://{url#authority}{url#normalizedPath}{Bucket}",
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
                                                                                "s3",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegion": interpolate(
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        }
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is False
                                                ):
                                                    if not (
                                                        string_equals(
                                                            p.Region,
                                                            interpolate(
                                                                "aws-global", p, _locals
                                                            ),
                                                        )
                                                    ):
                                                        if p.UseGlobalEndpoint is True:
                                                            if string_equals(
                                                                p.Region,
                                                                interpolate(
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ):
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "{url#scheme}://{Bucket}.{url#authority}{url#path}",
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
                                                                                    "s3",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                "signingRegion": interpolate(
                                                                                    "{Region}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            }
                                                                        ]
                                                                    },
                                                                    headers={},
                                                                )
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "{url#scheme}://{Bucket}.{url#authority}{url#path}",
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
                                                                                "s3",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegion": interpolate(
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        }
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is True
                                                ):
                                                    if not (
                                                        string_equals(
                                                            p.Region,
                                                            interpolate(
                                                                "aws-global", p, _locals
                                                            ),
                                                        )
                                                    ):
                                                        if p.UseGlobalEndpoint is False:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "{url#scheme}://{url#authority}{url#normalizedPath}{Bucket}",
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
                                                                                "s3",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegion": interpolate(
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        }
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if p.Endpoint is not None:
                                            _locals["url"] = parse_url(p.Endpoint)
                                            if _locals["url"] is not None:
                                                if (
                                                    get_attr(
                                                        _locals["url"],
                                                        interpolate("isIp", p, _locals),
                                                    )
                                                    is False
                                                ):
                                                    if not (
                                                        string_equals(
                                                            p.Region,
                                                            interpolate(
                                                                "aws-global", p, _locals
                                                            ),
                                                        )
                                                    ):
                                                        if p.UseGlobalEndpoint is False:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "{url#scheme}://{Bucket}.{url#authority}{url#path}",
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
                                                                                "s3",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            "signingRegion": interpolate(
                                                                                "{Region}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        }
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3-accelerate.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    if string_equals(
                                                        p.Region,
                                                        interpolate(
                                                            "us-east-1", p, _locals
                                                        ),
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3-accelerate.{partitionResult#dnsSuffix}",
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
                                                                            "s3",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ]
                                                            },
                                                            headers={},
                                                        )
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-accelerate.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is True:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3-accelerate.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{Bucket}.s3.{partitionResult#dnsSuffix}",
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
                                                                    "us-east-1",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is True:
                                                    if string_equals(
                                                        p.Region,
                                                        interpolate(
                                                            "us-east-1", p, _locals
                                                        ),
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{Bucket}.s3.{partitionResult#dnsSuffix}",
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
                                                                            "s3",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        "signingRegion": interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    }
                                                                ]
                                                            },
                                                            headers={},
                                                        )
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                            if p.UseDualStack is False:
                                if p.UseFIPS is False:
                                    if p.Accelerate is False:
                                        if not (p.Endpoint is not None):
                                            if not (
                                                string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "aws-global", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.UseGlobalEndpoint is False:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{Bucket}.s3.{Region}.{partitionResult#dnsSuffix}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                        raise EndpointError(
                            interpolate(
                                "Invalid region: region was not a valid DNS name.",
                                p,
                                _locals,
                            )
                        )
            if p.Endpoint is not None:
                _locals["url"] = parse_url(p.Endpoint)
                if _locals["url"] is not None:
                    if string_equals(
                        get_attr(_locals["url"], interpolate("scheme", p, _locals)),
                        interpolate("http", p, _locals),
                    ):
                        if aws_is_virtual_hostable_s3_bucket(p.Bucket, True):
                            if p.ForcePathStyle is False:
                                if p.UseFIPS is False:
                                    if p.UseDualStack is False:
                                        if p.Accelerate is False:
                                            _locals["partitionResult"] = aws_partition(
                                                p.Region
                                            )
                                            if _locals["partitionResult"] is not None:
                                                if is_valid_host_label(p.Region, False):
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "{url#scheme}://{Bucket}.{url#authority}{url#path}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid region: region was not a valid DNS name.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
            if p.ForcePathStyle is False:
                _locals["bucketArn"] = aws_parse_arn(p.Bucket)
                if _locals["bucketArn"] is not None:
                    _locals["arnType"] = get_attr(
                        _locals["bucketArn"], interpolate("resourceId[0]", p, _locals)
                    )
                    if _locals["arnType"] is not None:
                        if not (
                            string_equals(
                                _locals["arnType"], interpolate("", p, _locals)
                            )
                        ):
                            if string_equals(
                                get_attr(
                                    _locals["bucketArn"],
                                    interpolate("service", p, _locals),
                                ),
                                interpolate("s3-object-lambda", p, _locals),
                            ):
                                if string_equals(
                                    _locals["arnType"],
                                    interpolate("accesspoint", p, _locals),
                                ):
                                    _locals["accessPointName"] = get_attr(
                                        _locals["bucketArn"],
                                        interpolate("resourceId[1]", p, _locals),
                                    )
                                    if _locals["accessPointName"] is not None:
                                        if not (
                                            string_equals(
                                                _locals["accessPointName"],
                                                interpolate("", p, _locals),
                                            )
                                        ):
                                            if p.UseDualStack is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "S3 Object Lambda does not support Dual-stack",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            if p.Accelerate is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "S3 Object Lambda does not support S3 Accelerate",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            if not (
                                                string_equals(
                                                    get_attr(
                                                        _locals["bucketArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    interpolate("", p, _locals),
                                                )
                                            ):
                                                if p.DisableAccessPoints is not None:
                                                    if p.DisableAccessPoints is True:
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Access points are not supported for this operation",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                if not (
                                                    get_attr(
                                                        _locals["bucketArn"],
                                                        interpolate(
                                                            "resourceId[2]", p, _locals
                                                        ),
                                                    )
                                                    is not None
                                                ):
                                                    if p.UseArnRegion is not None:
                                                        if p.UseArnRegion is False:
                                                            if not (
                                                                string_equals(
                                                                    get_attr(
                                                                        _locals[
                                                                            "bucketArn"
                                                                        ],
                                                                        interpolate(
                                                                            "region",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ),
                                                                    interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            ):
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid configuration: region from ARN `{bucketArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                    _locals["bucketPartition"] = (
                                                        aws_partition(
                                                            get_attr(
                                                                _locals["bucketArn"],
                                                                interpolate(
                                                                    "region", p, _locals
                                                                ),
                                                            )
                                                        )
                                                    )
                                                    if (
                                                        _locals["bucketPartition"]
                                                        is not None
                                                    ):
                                                        _locals["partitionResult"] = (
                                                            aws_partition(p.Region)
                                                        )
                                                        if (
                                                            _locals["partitionResult"]
                                                            is not None
                                                        ):
                                                            if string_equals(
                                                                get_attr(
                                                                    _locals[
                                                                        "bucketPartition"
                                                                    ],
                                                                    interpolate(
                                                                        "name",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ),
                                                                get_attr(
                                                                    _locals[
                                                                        "partitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "name",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ),
                                                            ):
                                                                if is_valid_host_label(
                                                                    get_attr(
                                                                        _locals[
                                                                            "bucketArn"
                                                                        ],
                                                                        interpolate(
                                                                            "region",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ),
                                                                    True,
                                                                ):
                                                                    if string_equals(
                                                                        get_attr(
                                                                            _locals[
                                                                                "bucketArn"
                                                                            ],
                                                                            interpolate(
                                                                                "accountId",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        interpolate(
                                                                            "",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "Invalid ARN: Missing account id",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                    if is_valid_host_label(
                                                                        get_attr(
                                                                            _locals[
                                                                                "bucketArn"
                                                                            ],
                                                                            interpolate(
                                                                                "accountId",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        False,
                                                                    ):
                                                                        if is_valid_host_label(
                                                                            _locals[
                                                                                "accessPointName"
                                                                            ],
                                                                            False,
                                                                        ):
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
                                                                                            "{url#scheme}://{accessPointName}-{bucketArn#accountId}.{url#authority}{url#path}",
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
                                                                                                        "s3-object-lambda",
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
                                                                                        headers={},
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{accessPointName}-{bucketArn#accountId}.s3-object-lambda-fips.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                    "s3-object-lambda",
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
                                                                                    headers={},
                                                                                )
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{accessPointName}-{bucketArn#accountId}.s3-object-lambda.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                "s3-object-lambda",
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
                                                                                headers={},
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `{accessPointName}`",
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
                                                                        "Invalid region in ARN: `{bucketArn#region}` (invalid DNS name)",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Client was configured for partition `{partitionResult#name}` but ARN (`{Bucket}`) has `{bucketPartition#name}`",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid ARN: The ARN may only contain a single resource component after `accesspoint`.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: bucket ARN is missing a region",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Expected a resource of the format `accesspoint:<accesspoint name>` but no name was provided",
                                            p,
                                            _locals,
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Object Lambda ARNs only support `accesspoint` arn types, but found: `{arnType}`",
                                        p,
                                        _locals,
                                    )
                                )
                            if string_equals(
                                _locals["arnType"],
                                interpolate("accesspoint", p, _locals),
                            ):
                                _locals["accessPointName"] = get_attr(
                                    _locals["bucketArn"],
                                    interpolate("resourceId[1]", p, _locals),
                                )
                                if _locals["accessPointName"] is not None:
                                    if not (
                                        string_equals(
                                            _locals["accessPointName"],
                                            interpolate("", p, _locals),
                                        )
                                    ):
                                        if not (
                                            string_equals(
                                                get_attr(
                                                    _locals["bucketArn"],
                                                    interpolate("region", p, _locals),
                                                ),
                                                interpolate("", p, _locals),
                                            )
                                        ):
                                            if string_equals(
                                                _locals["arnType"],
                                                interpolate("accesspoint", p, _locals),
                                            ):
                                                if not (
                                                    string_equals(
                                                        get_attr(
                                                            _locals["bucketArn"],
                                                            interpolate(
                                                                "region", p, _locals
                                                            ),
                                                        ),
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if (
                                                        p.DisableAccessPoints
                                                        is not None
                                                    ):
                                                        if (
                                                            p.DisableAccessPoints
                                                            is True
                                                        ):
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Access points are not supported for this operation",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                    if not (
                                                        get_attr(
                                                            _locals["bucketArn"],
                                                            interpolate(
                                                                "resourceId[2]",
                                                                p,
                                                                _locals,
                                                            ),
                                                        )
                                                        is not None
                                                    ):
                                                        if p.UseArnRegion is not None:
                                                            if p.UseArnRegion is False:
                                                                if not (
                                                                    string_equals(
                                                                        get_attr(
                                                                            _locals[
                                                                                "bucketArn"
                                                                            ],
                                                                            interpolate(
                                                                                "region",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        interpolate(
                                                                            "{Region}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                ):
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid configuration: region from ARN `{bucketArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                        _locals["bucketPartition"] = (
                                                            aws_partition(
                                                                get_attr(
                                                                    _locals[
                                                                        "bucketArn"
                                                                    ],
                                                                    interpolate(
                                                                        "region",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            )
                                                        )
                                                        if (
                                                            _locals["bucketPartition"]
                                                            is not None
                                                        ):
                                                            _locals[
                                                                "partitionResult"
                                                            ] = aws_partition(p.Region)
                                                            if (
                                                                _locals[
                                                                    "partitionResult"
                                                                ]
                                                                is not None
                                                            ):
                                                                if string_equals(
                                                                    get_attr(
                                                                        _locals[
                                                                            "bucketPartition"
                                                                        ],
                                                                        interpolate(
                                                                            "name",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ),
                                                                    interpolate(
                                                                        "{partitionResult#name}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ):
                                                                    if is_valid_host_label(
                                                                        get_attr(
                                                                            _locals[
                                                                                "bucketArn"
                                                                            ],
                                                                            interpolate(
                                                                                "region",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        True,
                                                                    ):
                                                                        if string_equals(
                                                                            get_attr(
                                                                                _locals[
                                                                                    "bucketArn"
                                                                                ],
                                                                                interpolate(
                                                                                    "service",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            ),
                                                                            interpolate(
                                                                                "s3",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ):
                                                                            if is_valid_host_label(
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "bucketArn"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "accountId",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                ),
                                                                                False,
                                                                            ):
                                                                                if is_valid_host_label(
                                                                                    _locals[
                                                                                        "accessPointName"
                                                                                    ],
                                                                                    False,
                                                                                ):
                                                                                    if (
                                                                                        p.Accelerate
                                                                                        is True
                                                                                    ):
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "Access Points do not support S3 Accelerate",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
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
                                                                                                    "https://{accessPointName}-{bucketArn#accountId}.s3-accesspoint-fips.dualstack.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                                "s3",
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
                                                                                                headers={},
                                                                                            )
                                                                                    if (
                                                                                        p.UseFIPS
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            p.UseDualStack
                                                                                            is False
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{accessPointName}-{bucketArn#accountId}.s3-accesspoint-fips.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                                "s3",
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
                                                                                                headers={},
                                                                                            )
                                                                                    if (
                                                                                        p.UseFIPS
                                                                                        is False
                                                                                    ):
                                                                                        if (
                                                                                            p.UseDualStack
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{accessPointName}-{bucketArn#accountId}.s3-accesspoint.dualstack.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                                "s3",
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
                                                                                                headers={},
                                                                                            )
                                                                                    if (
                                                                                        p.UseFIPS
                                                                                        is False
                                                                                    ):
                                                                                        if (
                                                                                            p.UseDualStack
                                                                                            is False
                                                                                        ):
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
                                                                                                            "{url#scheme}://{accessPointName}-{bucketArn#accountId}.{url#authority}{url#path}",
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
                                                                                                                        "s3",
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
                                                                                                        headers={},
                                                                                                    )
                                                                                    if (
                                                                                        p.UseFIPS
                                                                                        is False
                                                                                    ):
                                                                                        if (
                                                                                            p.UseDualStack
                                                                                            is False
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{accessPointName}-{bucketArn#accountId}.s3-accesspoint.{bucketArn#region}.{bucketPartition#dnsSuffix}",
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
                                                                                                                "s3",
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
                                                                                                headers={},
                                                                                            )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `{accessPointName}`",
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
                                                                                "Invalid ARN: The ARN was not for the S3 service, found: {bucketArn#service}",
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
                                                                        "Client was configured for partition `{partitionResult#name}` but ARN (`{Bucket}`) has `{bucketPartition#name}`",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: The ARN may only contain a single resource component after `accesspoint`.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                        if is_valid_host_label(
                                            _locals["accessPointName"], True
                                        ):
                                            if p.UseDualStack is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "S3 MRAP does not support dual-stack",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            if p.UseFIPS is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "S3 MRAP does not support FIPS",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            if p.Accelerate is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "S3 MRAP does not support S3 Accelerate",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            if p.DisableMultiRegionAccessPoints is True:
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid configuration: Multi-Region Access Point ARNs are disabled.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            _locals["mrapPartition"] = aws_partition(
                                                p.Region
                                            )
                                            if _locals["mrapPartition"] is not None:
                                                if string_equals(
                                                    get_attr(
                                                        _locals["mrapPartition"],
                                                        interpolate("name", p, _locals),
                                                    ),
                                                    get_attr(
                                                        _locals["bucketArn"],
                                                        interpolate(
                                                            "partition", p, _locals
                                                        ),
                                                    ),
                                                ):
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{accessPointName}.accesspoint.s3-global.{mrapPartition#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={
                                                            "authSchemes": [
                                                                {
                                                                    "disableDoubleEncoding": True,
                                                                    "name": interpolate(
                                                                        "sigv4a",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    "signingName": interpolate(
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegionSet": [
                                                                        interpolate(
                                                                            "*",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    ],
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Client was configured for partition `{mrapPartition#name}` but bucket referred to partition `{bucketArn#partition}`",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Access Point Name", p, _locals
                                            )
                                        )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Expected a resource of the format `accesspoint:<accesspoint name>` but no name was provided",
                                        p,
                                        _locals,
                                    )
                                )
                            if string_equals(
                                get_attr(
                                    _locals["bucketArn"],
                                    interpolate("service", p, _locals),
                                ),
                                interpolate("s3-outposts", p, _locals),
                            ):
                                if p.UseDualStack is True:
                                    raise EndpointError(
                                        interpolate(
                                            "S3 Outposts does not support Dual-stack",
                                            p,
                                            _locals,
                                        )
                                    )
                                if p.UseFIPS is True:
                                    raise EndpointError(
                                        interpolate(
                                            "S3 Outposts does not support FIPS",
                                            p,
                                            _locals,
                                        )
                                    )
                                if p.Accelerate is True:
                                    raise EndpointError(
                                        interpolate(
                                            "S3 Outposts does not support S3 Accelerate",
                                            p,
                                            _locals,
                                        )
                                    )
                                if (
                                    get_attr(
                                        _locals["bucketArn"],
                                        interpolate("resourceId[4]", p, _locals),
                                    )
                                    is not None
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid Arn: Outpost Access Point ARN contains sub resources",
                                            p,
                                            _locals,
                                        )
                                    )
                                _locals["outpostId"] = get_attr(
                                    _locals["bucketArn"],
                                    interpolate("resourceId[1]", p, _locals),
                                )
                                if _locals["outpostId"] is not None:
                                    if is_valid_host_label(_locals["outpostId"], False):
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
                                                        interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    )
                                                ):
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid configuration: region from ARN `{bucketArn#region}` does not match client region `{Region}` and UseArnRegion is `false`",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                        _locals["bucketPartition"] = aws_partition(
                                            get_attr(
                                                _locals["bucketArn"],
                                                interpolate("region", p, _locals),
                                            )
                                        )
                                        if _locals["bucketPartition"] is not None:
                                            _locals["partitionResult"] = aws_partition(
                                                p.Region
                                            )
                                            if _locals["partitionResult"] is not None:
                                                if string_equals(
                                                    get_attr(
                                                        _locals["bucketPartition"],
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
                                                                    "accessPointName"
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
                                                                        if is_valid_host_label(
                                                                            _locals[
                                                                                "accessPointName"
                                                                            ],
                                                                            False,
                                                                        ):
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
                                                                                            "https://{accessPointName}-{bucketArn#accountId}.{outpostId}.{url#authority}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={
                                                                                            "authSchemes": [
                                                                                                {
                                                                                                    "disableDoubleEncoding": True,
                                                                                                    "name": interpolate(
                                                                                                        "sigv4a",
                                                                                                        p,
                                                                                                        _locals,
                                                                                                    ),
                                                                                                    "signingName": interpolate(
                                                                                                        "s3-outposts",
                                                                                                        p,
                                                                                                        _locals,
                                                                                                    ),
                                                                                                    "signingRegionSet": [
                                                                                                        interpolate(
                                                                                                            "*",
                                                                                                            p,
                                                                                                            _locals,
                                                                                                        )
                                                                                                    ],
                                                                                                },
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
                                                                                                },
                                                                                            ]
                                                                                        },
                                                                                        headers={},
                                                                                    )
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{accessPointName}-{bucketArn#accountId}.{outpostId}.s3-outposts.{bucketArn#region}.{bucketPartition#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={
                                                                                    "authSchemes": [
                                                                                        {
                                                                                            "disableDoubleEncoding": True,
                                                                                            "name": interpolate(
                                                                                                "sigv4a",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingName": interpolate(
                                                                                                "s3-outposts",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            "signingRegionSet": [
                                                                                                interpolate(
                                                                                                    "*",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                )
                                                                                            ],
                                                                                        },
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
                                                                                        },
                                                                                    ]
                                                                                },
                                                                                headers={},
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `{accessPointName}`",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Expected an outpost type `accesspoint`, found {outpostType}",
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
                                                                "Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `{bucketArn#accountId}`",
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
                                                        "Client was configured for partition `{partitionResult#name}` but ARN (`{Bucket}`) has `{bucketPartition#name}`",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: The outpost Id may only contain a-z, A-Z, 0-9 and `-`. Found: `{outpostId}`",
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
                                interpolate(
                                    "Invalid ARN: Unrecognized format: {Bucket} (type: {arnType})",
                                    p,
                                    _locals,
                                )
                            )
                    raise EndpointError(
                        interpolate("Invalid ARN: No ARN type specified", p, _locals)
                    )
            _locals["arnPrefix"] = substring(p.Bucket, 0, 4, False)
            if _locals["arnPrefix"] is not None:
                if string_equals(_locals["arnPrefix"], interpolate("arn:", p, _locals)):
                    if not (aws_parse_arn(p.Bucket) is not None):
                        raise EndpointError(
                            interpolate(
                                "Invalid ARN: `{Bucket}` was not a valid ARN",
                                p,
                                _locals,
                            )
                        )
            if p.ForcePathStyle is True:
                if aws_parse_arn(p.Bucket):
                    raise EndpointError(
                        interpolate(
                            "Path-style addressing cannot be used with ARN buckets",
                            p,
                            _locals,
                        )
                    )
            _locals["uri_encoded_bucket"] = uri_encode(p.Bucket)
            if _locals["uri_encoded_bucket"] is not None:
                _locals["partitionResult"] = aws_partition(p.Region)
                if _locals["partitionResult"] is not None:
                    if p.Accelerate is False:
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.dualstack.us-east-1.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                                                            "us-east-1", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is True:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is False:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.us-east-1.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                                                            "us-east-1", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is True:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3-fips.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is True:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is False:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3-fips.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3.dualstack.us-east-1.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                                                            "us-east-1", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is True:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is False:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3.dualstack.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is False:
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if p.UseFIPS is False:
                                        if string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        ):
                                            return Endpoint(
                                                url=interpolate(
                                                    "{url#scheme}://{url#authority}{url#normalizedPath}{uri_encoded_bucket}",
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
                                                                "us-east-1", p, _locals
                                                            ),
                                                        }
                                                    ]
                                                },
                                                headers={},
                                            )
                        if p.UseDualStack is False:
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if p.UseFIPS is False:
                                        if not (
                                            string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            )
                                        ):
                                            if p.UseGlobalEndpoint is True:
                                                if string_equals(
                                                    p.Region,
                                                    interpolate(
                                                        "us-east-1", p, _locals
                                                    ),
                                                ):
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "{url#scheme}://{url#authority}{url#normalizedPath}{uri_encoded_bucket}",
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
                                                                        "s3", p, _locals
                                                                    ),
                                                                    "signingRegion": interpolate(
                                                                        "{Region}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                }
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                                                return Endpoint(
                                                    url=interpolate(
                                                        "{url#scheme}://{url#authority}{url#normalizedPath}{uri_encoded_bucket}",
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
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                        if p.UseDualStack is False:
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if p.UseFIPS is False:
                                        if not (
                                            string_equals(
                                                p.Region,
                                                interpolate("aws-global", p, _locals),
                                            )
                                        ):
                                            if p.UseGlobalEndpoint is False:
                                                return Endpoint(
                                                    url=interpolate(
                                                        "{url#scheme}://{url#authority}{url#normalizedPath}{uri_encoded_bucket}",
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
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    ):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                                                            "us-east-1", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is True:
                                            if string_equals(
                                                p.Region,
                                                interpolate("us-east-1", p, _locals),
                                            ):
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://s3.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if p.UseFIPS is False:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is False:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3.{Region}.{partitionResult#dnsSuffix}/{uri_encoded_bucket}",
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
                    raise EndpointError(
                        interpolate(
                            "Path-style addressing cannot be used with S3 Accelerate",
                            p,
                            _locals,
                        )
                    )
        if p.UseObjectLambdaEndpoint is not None:
            if p.UseObjectLambdaEndpoint is True:
                _locals["partitionResult"] = aws_partition(p.Region)
                if _locals["partitionResult"] is not None:
                    if is_valid_host_label(p.Region, True):
                        if p.UseDualStack is True:
                            raise EndpointError(
                                interpolate(
                                    "S3 Object Lambda does not support Dual-stack",
                                    p,
                                    _locals,
                                )
                            )
                        if p.Accelerate is True:
                            raise EndpointError(
                                interpolate(
                                    "S3 Object Lambda does not support S3 Accelerate",
                                    p,
                                    _locals,
                                )
                            )
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
                                                "name": interpolate(
                                                    "sigv4", p, _locals
                                                ),
                                                "signingName": interpolate(
                                                    "s3-object-lambda", p, _locals
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
                                    "https://s3-object-lambda-fips.{Region}.{partitionResult#dnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={
                                    "authSchemes": [
                                        {
                                            "disableDoubleEncoding": True,
                                            "name": interpolate("sigv4", p, _locals),
                                            "signingName": interpolate(
                                                "s3-object-lambda", p, _locals
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
                                "https://s3-object-lambda.{Region}.{partitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "disableDoubleEncoding": True,
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "s3-object-lambda", p, _locals
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
                            "Invalid region: region was not a valid DNS name.",
                            p,
                            _locals,
                        )
                    )
        if not (p.Bucket is not None):
            _locals["partitionResult"] = aws_partition(p.Region)
            if _locals["partitionResult"] is not None:
                if is_valid_host_label(p.Region, True):
                    if p.UseFIPS is True:
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if string_equals(
                                    p.Region, interpolate("aws-global", p, _locals)
                                ):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3-fips.dualstack.us-east-1.{partitionResult#dnsSuffix}",
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
                                                        "us-east-1", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                    if p.UseFIPS is True:
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is False:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if string_equals(
                                    p.Region, interpolate("aws-global", p, _locals)
                                ):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3-fips.us-east-1.{partitionResult#dnsSuffix}",
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
                                                        "us-east-1", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                    if p.UseFIPS is True:
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is False:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3-fips.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if string_equals(
                                    p.Region, interpolate("aws-global", p, _locals)
                                ):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3.dualstack.us-east-1.{partitionResult#dnsSuffix}",
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
                                                        "us-east-1", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                    if p.UseFIPS is False:
                        if p.UseDualStack is True:
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is True:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is False:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3.dualstack.{Region}.{partitionResult#dnsSuffix}",
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
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
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
                                                            "sigv4", p, _locals
                                                        ),
                                                        "signingName": interpolate(
                                                            "s3", p, _locals
                                                        ),
                                                        "signingRegion": interpolate(
                                                            "us-east-1", p, _locals
                                                        ),
                                                    }
                                                ]
                                            },
                                            headers={},
                                        )
                    if p.UseFIPS is False:
                        if p.UseDualStack is False:
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is True:
                                            if string_equals(
                                                p.Region,
                                                interpolate("us-east-1", p, _locals),
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
                                                                    "sigv4", p, _locals
                                                                ),
                                                                "signingName": interpolate(
                                                                    "s3", p, _locals
                                                                ),
                                                                "signingRegion": interpolate(
                                                                    "{Region}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            }
                                                        ]
                                                    },
                                                    headers={},
                                                )
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
                            if p.Endpoint is not None:
                                _locals["url"] = parse_url(p.Endpoint)
                                if _locals["url"] is not None:
                                    if not (
                                        string_equals(
                                            p.Region,
                                            interpolate("aws-global", p, _locals),
                                        )
                                    ):
                                        if p.UseGlobalEndpoint is False:
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
                            if not (p.Endpoint is not None):
                                if string_equals(
                                    p.Region, interpolate("aws-global", p, _locals)
                                ):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://s3.{partitionResult#dnsSuffix}",
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
                                                        "us-east-1", p, _locals
                                                    ),
                                                }
                                            ]
                                        },
                                        headers={},
                                    )
                    if p.UseFIPS is False:
                        if p.UseDualStack is False:
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is True:
                                        if string_equals(
                                            p.Region,
                                            interpolate("us-east-1", p, _locals),
                                        ):
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://s3.{partitionResult#dnsSuffix}",
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
                                                "https://s3.{Region}.{partitionResult#dnsSuffix}",
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
                            if not (p.Endpoint is not None):
                                if not (
                                    string_equals(
                                        p.Region, interpolate("aws-global", p, _locals)
                                    )
                                ):
                                    if p.UseGlobalEndpoint is False:
                                        return Endpoint(
                                            url=interpolate(
                                                "https://s3.{Region}.{partitionResult#dnsSuffix}",
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
                raise EndpointError(
                    interpolate(
                        "Invalid region: region was not a valid DNS name.", p, _locals
                    )
                )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("A region must be set when sending requests to S3.", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
